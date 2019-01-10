PYTHON Shell:

import requests, json


<<< Retrieve list of tasks >>>
requests.get('http://localhost:5000/todos').json()

<<< Retrieve a task >>>
requests.get('http://localhost:5000/todos/1').json()

<<< Create a new task >>>
requests.post('http://localhost:5000/todos',
               headers={'Content-Type': 'application/json'},
               data=json.dumps({'task': 'go outside!'})).json()

<<< Update an existing task >>>
requests.put('http://localhost:5000/todos/1',
              headers={'Content-Type': 'application/json'},
              data=json.dumps({'task': 'go to the gym'})).json()

<<< Delete a task >>>
requests.delete('http://localhost:5000/todos/1')

