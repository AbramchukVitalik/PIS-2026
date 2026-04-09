from fastapi.testclient import TestClient
from infrastructure.adapter.inbound.note_controller import app

client = TestClient(app)


def test_create_note():
    response = client.post("/notes", json={
        "notebook_id": "1",
        "author_id": "1",
        "content": "Hello world"
    })

    assert response.status_code == 200
    assert "id" in response.json()


def test_get_note():
    create = client.post("/notes", json={
        "notebook_id": "1",
        "author_id": "1",
        "content": "B"
    })

    note_id = create.json()["id"]

    response = client.get(f"/notes/{note_id}")

    assert response.status_code == 200
    assert response.json()["id"] == note_id