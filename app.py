#!/usr/bin/python3
#!flask/bin/python3
"""
A Flask application
version: 1.0
"""
from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Mbatata, Chigumu,  Fruit, Chitumbuwa',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find good Python tutorial on the web',
        'done': False
    }
]


@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=['GET'],strict_slashes=False)
def get_tasks(task_id):
    """Displays all tasks"""
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'tasks': task[0]})


@app.errorhandler(404)
def not_found(error):
    """Returns 404 response"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/todo/api/v1.0/task', methods=['POST'], strict_slashes=False)
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': task[-1]['id'] + 1,   # create a new task dictionary, using the id of the last task plus one
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
