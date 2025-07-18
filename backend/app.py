from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # فعال کردن CORS برای همه روت‌ها

DATA_FILE = 'tasks.json'

# اگر فایل JSON وجود نداشت بسازش
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def read_tasks():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def write_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = read_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json
    tasks = read_tasks()
    tasks.append(new_task)
    write_tasks(tasks)
    return jsonify(new_task), 201

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    tasks = read_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        write_tasks(tasks)
        return jsonify(removed_task)
    else:
        return jsonify({"error": "Task not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

