from fastapi.testclient import TestClient

# from .main import app

client = TestClient

def setup_functions():
    pass

def test_post_compute():
    data = {
        "batch_id": "id0102a",
        "payload": [[1,2], [3,4]]
    }
    response = client.post(url='/compute', json=data)
    assert response.status_code == 200
    assert response.json["status"] == "complete"

def test_get_result():
    batch_id = "id0102a"
    response = client.post(url=f'/compute/{batch_id}')
    assert response.status_code == 200
