from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data - database la treat chey
tasks = [
    {'id': 1, 'title': 'Learn Python Basics', 'status': 'pending'},
    {'id': 2, 'title': 'Build Flask API', 'status': 'in-progress'}
]

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    return jsonify({'success': True, 'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'status': 'pending'
    }
    tasks.append(new_task)
    return jsonify({'success': True, 'task': new_task}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
