from models import Todo

from flask import Flask, jsonify, abort, make_response
from flask_restful import reqparse, abort, Resource, fields, marshal_with
from flask_httpauth import HTTPBasicAuth

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


""" ######## """
""" database """
""" ######## """

# database login
Session = sessionmaker(autocommit = False,
                       autoflush  = False,
                       bind       = create_engine('mysql+pymysql://python:python@localhost/python'))
session = scoped_session(Session)

# table structure
user_fields = {'id'      : fields.Integer,
               'username': fields.String,
               'email'   : fields.String,
               'password': fields.String, 
               'uri'     : fields.Url('user', absolute=True),
               }

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('email',    type=str)
parser.add_argument('password', type=str)


""" ################ """
""" authentification """
""" ################ """

auth = HTTPBasicAuth()

# definate user
USER_DATA = {"admin": "SuperSecretPwd"}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)


""" ######### """
""" functions """
""" ######### """

# specific entry
class TodoResource(Resource):
    decorators = [auth.login_required]

    # IMPORTANT:
    # use requests in the editor
    # first steps: import requests, json 
    #              from requests.auth import HTTPBasicAuth

    @marshal_with(user_fields)

    # <<< Retrieve a task >>>   
    # requests.get('http://localhost:5000/api/resource/8', 
    #               auth=HTTPBasicAuth('admin', 'SuperSecretPwd')).json() 
 
    def get(self, id):
        todo = session.query(Todo).filter(Todo.id == id).first()
        if not todo:
            abort(404, message="User {} doesn't exist".format(id))
        return todo


    # <<< Delete a task >>>
    # requests.delete('http://localhost:5000/api/resource/8', 
    #                  auth=HTTPBasicAuth('admin', 'SuperSecretPwd')).json() 

    def delete(self, id):
        todo = session.query(Todo).filter(Todo.id == id).first()
        if not todo:
            return "ID {} doesn't exist".format(id)
        session.delete(todo)
        session.commit()
        return "ID {} deleted".format(id)


    # <<< Update an existing task >>>
    # requests.put('http://localhost:5000/api/resource/1', 
    #               auth=HTTPBasicAuth('admin', 'SuperSecretPwd'),
    #               headers={'Content-Type': 'application/json'},
    #               data=json.dumps({'email': 'go away'})).json()

    @marshal_with(user_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        todo = session.query(Todo).filter(Todo.id == id).first()
        
        if (parsed_args['username']) is not None:
            todo.username = parsed_args['username']
        if (parsed_args['email']) is not None:    
            todo.email = parsed_args['email']
        if (parsed_args['password']) is not None:  
            todo.password = parsed_args['password']

        session.add(todo)
        session.commit()
        return todo, 201


# all entries
class TodoListResource(Resource):
    decorators = [auth.login_required] 


    # <<< Retrieve list of tasks >>>
    # requests.get('http://localhost:5000/api/resource', 
    #               auth=HTTPBasicAuth('admin', 'SuperSecretPwd')).json() 

    @marshal_with(user_fields)
    def get(self):
        todo = session.query(Todo).all()
        return todo


    # <<< Create a new task >>>
    # requests.post('http://localhost:5000/api/resource',
    #                headers={'Content-Type': 'application/json'},
    #                auth=HTTPBasicAuth('admin', 'SuperSecretPwd'),
    #                data=json.dumps({'username': 'Muster', 
    #                                 'email': 'max@gmx.de', 
    #                                 'password': 'geheim'})).json()

    @marshal_with(user_fields)
    def post(self):
        parsed_args = parser.parse_args()
        todo = Todo(username = parsed_args['username'],
                    email    = parsed_args['email'],
                    password = parsed_args['password'])
        session.add(todo)
        session.commit()
        return todo, 201
