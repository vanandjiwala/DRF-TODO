import requests
import tests.testconfig as config


def test_post_task_201():
    task_data = {
        "title": "My Task",
        "description": "My Task Description",
        "completed": False
    }
    url = "".join([config.base_url,'tasks/'])
    response = requests.post(url,task_data)
    assert response.status_code == 201

def test_post_task_wothout_completed():
    task_data = {
        "title": "My Task",
        "description": "My Task Description"
    }
    url = "".join([config.base_url,'tasks/'])
    response = requests.post(url,task_data)
    assert response.status_code == 201

def test_get_tasks_200():
    response = requests.get("http://localhost:8000/api/tasks/")
    assert response.status_code == 200


def test_get_task_200():
    task_data = {
        "title": "Task for get test",
        "description": "get task description",
        "completed": False
    }
    response = requests.post("http://localhost:8000/api/tasks/",task_data)
    task_id = response.json().get('id')
    url = "".join([config.base_url, 'tasks/',str(task_id)])
    response = requests.get(url)
    assert response.status_code == 200

def test_update_task_200():
    task_data = {
        "title": "Task for put test",
        "description": "get task description",
        "completed": False
    }
    response = requests.post("http://localhost:8000/api/tasks/",task_data)
    task_id = response.json().get('id')
    url = "".join([config.base_url, 'tasks/',str(task_id),"/"])
    put_data = {
        "title": "Task for put test 1 ",
        "description": "put description",
        "completed": True
    }

    response = requests.put(url,put_data)
    assert response.status_code == 200

def test_update_task_200():
    task_data = {
        "title": "Task for delete test",
        "description": "get task description",
        "completed": False
    }
    response = requests.post("http://localhost:8000/api/tasks/",task_data)
    task_id = response.json().get('id')
    url = "".join([config.base_url, 'tasks/',str(task_id),"/"])
    response = requests.delete(url)
    assert response.status_code == 204

