import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

@pytest.fixture
def task_data():
    return {
        'title': 'Tarefa de teste',
        'description': 'Descrição da tarefa de teste'
    }

def test_create_task(task_data):
    response = requests.post(f'{BASE_URL}/tasks', json=task_data)
    assert response.status_code == 201

    response_json = response.json()
    assert 'message' in response_json
    assert 'id' in response_json

def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    assert response.status_code == 200
    response_json = response.json()

    assert 'tasks' in response_json
    assert isinstance(response_json['tasks'], list)
    assert 'total_tasks' in response_json

def test_get_task():
    # Cria uma nova tarefa
    task_data = {'title': 'Consulta tarefa', 'description': 'Consulta'}
    create_resp = requests.post(f'{BASE_URL}/tasks', json=task_data)
    assert create_resp.status_code == 201

    task_id = create_resp.json()['id']  # pega o id localmente

    response = requests.get(f'{BASE_URL}/tasks/{task_id}')
    assert response.status_code == 200

    response_json = response.json()
    assert response_json['id'] == task_id
    assert response_json['title'] == task_data['title']

def test_update_task():
    task_data = {'title': 'Tarefa update', 'description': 'Antes do update'}
    create_resp = requests.post(f'{BASE_URL}/tasks', json=task_data)
    task_id = create_resp.json()['id']

    payload = {
        'title': 'Tarefa atualizada',
        'description': 'Descrição atualizada',
        'completed': True
    }

    update_resp = requests.put(f'{BASE_URL}/tasks/{task_id}', json=payload)
    assert update_resp.status_code == 200

    # Validação do conteúdo atualizado
    get_resp = requests.get(f'{BASE_URL}/tasks/{task_id}')
    task = get_resp.json()
    assert task['title'] == payload['title']
    assert task['description'] == payload['description']
    assert task['completed'] == payload['completed']

def test_delete_task():
    task_data = {'title': 'Tarefa deletar', 'description': 'Será removida'}
    create_resp = requests.post(f'{BASE_URL}/tasks', json=task_data)
    task_id = create_resp.json()['id']

    delete_resp = requests.delete(f'{BASE_URL}/tasks/{task_id}')
    assert delete_resp.status_code == 200

    # Verifica se foi deletada de fato
    get_resp = requests.get(f'{BASE_URL}/tasks/{task_id}')
    assert get_resp.status_code == 404

def test_task_not_found():
    response = requests.get(f'{BASE_URL}/tasks/99999')
    assert response.status_code == 404
    assert 'message' in response.json()