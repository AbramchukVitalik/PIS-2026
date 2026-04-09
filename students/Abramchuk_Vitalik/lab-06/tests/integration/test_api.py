from fastapi.testclient import TestClient
from infrastructure.api.note_controller import app

client = TestClient(app)


def test_create_and_get_note():
    response = client.post("/notes", json={
        "notebook_id": "1",
        "author_id": "1",
        "content": "hello"
    })

    assert response.status_code == 200
    note_id = response.json()["id"]

    get = client.get(f"/notes/{note_id}")

    assert get.status_code == 200
    assert get.json()["id"] == note_id