# https://github.com/mmautner/simple_api
# https://github.com/miguelgrinberg/REST-tutorial
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
# http://polyglot.ninja/securing-rest-apis-basic-http-authentication-python-flask/

#!/usr/bin/env python

from flask import Flask
from flask_restful import Api

from resources import TodoListResource, TodoResource


app = Flask(__name__)
api = Api(app)

api.add_resource(TodoListResource, '/api/resource', endpoint='users')
api.add_resource(TodoResource, '/api/resource/<string:id>', endpoint='user')


if __name__ == '__main__':
    app.run(debug=True)
