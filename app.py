from flask import Flask, request, jsonify
from models.task import Task
import logging

app = Flask(__name__)

# Setup de log
logging.basicConfig(level=logging.INFO)

# Armazenamento temporário (memória)
tasks = []
task_id_control = 1

def find_task(task_id):
    return next((t for t in tasks if t.id == task_id), None)

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "JSON inválido"}), 400

    if not data or 'title' not in data:
        return jsonify({"error": "Campo 'title' é obrigatório"}), 400

    new_task = Task(
        id=task_id_control,
        title=data['title'],
        description=data.get('description', '')
    )
    task_id_control += 1
    tasks.append(new_task)

    logging.info(f"Tarefa criada: {new_task}")

    return jsonify({
        'message': 'Tarefa criada com sucesso!',
        'id': new_task.id
    }), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = find_task(task_id)
    if task:
        return jsonify(task.to_dict())
    return jsonify({'message': 'Tarefa não encontrada!'}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = find_task(task_id)
    if not task:
        return jsonify({'message': 'Tarefa não encontrada!'}), 404

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "JSON inválido"}), 400

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)

    logging.info(f"Tarefa atualizada: {task}")

    return jsonify({
        'message': 'Tarefa atualizada com sucesso!'
    })

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = find_task(task_id)
    if not task:
        return jsonify({'message': 'Tarefa não encontrada!'}), 404

    tasks.remove(task)

    return jsonify({
        'message': 'Tarefa removida com sucesso!'
    })

if __name__ == '__main__':
    app.run(debug=True)