import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():

    new_task_data = {
        "title": "Task 1",
        "description": "This is task 1"
    }

    response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
    assert response.status_code == 200
    assert "message" in response.json()
    assert "id" in response.json()
    tasks.append(response.json()["id"])

def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    assert response.status_code == 200

def test_get_task_by_id():
    response = requests.get(f'{BASE_URL}/tasks/1')
    assert response.status_code == 200

def test_update_task():
    updated_task_data = {
        "title": "Task 1",
        "description": "This is task 1",
        "completed": True
    }

    response = requests.put(f'{BASE_URL}/tasks/1', json=updated_task_data)
    assert response.status_code == 200

def test_delete_task():
    response = requests.delete(f'{BASE_URL}/tasks/1')
    assert response.status_code == 200



