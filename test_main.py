from fastapi.testclient import TestClient

from .main import app

client = TestClient

def setup_functions():
    pass

def test_post_compute():
    data = {
        "batchid": "id0102a",
        "payload": [[1,2], [3,4]]
    }
    response = client.post('/compute', json=data)
    assert response.status_code == 200
    assert response.json["status"] == "complete"

def test_get_result():
    batchid = "id0102a"
    response = client.post(f'/compute/{batchid}')
    assert response.status_code == 200
