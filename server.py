from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Flask", "description": "Study Flask framework"},
    {"id": 2, "title": "Build a REST API", "description": "Create a simple REST API"}
]


@app.route('/tasks/', methods=['GET'])
def all_tasks():
    return jsonify(tasks)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def particular_task(task_id):
    data = [task for task in tasks if task['id'] == task_id]
    return jsonify(data[0])


@app.route('/tasks/', methods=['POST'])
def get_item():
    data = request.get_json()
    val = max(tasks, key=lambda k: k['id'], default={'id': 1})['id']
    data['id'] = val + 1
    tasks.append(data)
    return jsonify(data), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    tasks.remove([task for task in tasks if task['id'] == task_id][0])
    val = max(tasks, key=lambda k: k['id'], default={'id': 1})['id']
    data['id'] = val + 1
    tasks.append(data)
    return jsonify(data)


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks.pop(task_id)
    return jsonify({"result": True}), 200


if __name__ == '__main__':
    app.run(debug=True)
