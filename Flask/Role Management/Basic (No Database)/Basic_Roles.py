# https://github.com/ownaginatious/flask-basic-roles

from flask import Flask
from flask_basic_roles import BasicRoleAuth
app = Flask(__name__)
auth = BasicRoleAuth()

# Let's add some users.
auth.add_user(user='bob', password='secret123', roles='producer')
auth.add_user(user='alice', password='drowssap', roles=('producer','consumer'))
auth.add_user(user='bill', password='54321')
auth.add_user(user='steve', password='12345', roles='admin')

#auth.load_from_file("./Python_Training/Bootcamp/Flask/Role Management/user.txt")



# Only producers and admins can post, while consumers can only get.
# Admins can also perform all other verbs.
@app.route("/task")
@auth.require(roles={
    'POST': 'producer',
    'GET': 'consumer',
    'DELETE,POST,PATCH,PUT,GET': 'admin'
})
def tasks_endpoint(methods=(...)):
    return "Here tasks get produced and consumed!"

# We can secure by user too. Steve can use any verb on this
# endpoint and everyone else is denied access.
@app.route("/task_status")
@auth.require(users='steve')
def task_status_endpoint(methods=(...)):
    return "Here are the task statuses!"

# Alice, Bill and users with an 'admin' role can access this, while everyone
# else is denied on all verbs.
@app.route("/task_failures")
@auth.require(users=('alice', 'bill'), roles='admin')
def task_failures(methods=(...)):
    return "Here are the task failures!"

# Everyone including unauthenticated users can view task results.
@app.route("/task_results")
def task_results(methods=(...)):
    return "Here are the task results!"

if __name__ == "__main__":
    app.run()