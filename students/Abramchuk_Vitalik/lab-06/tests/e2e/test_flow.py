from fastapi.testclient import TestClient
from infrastructure.api.note_controller import app

client = TestClient(app)


def test_full_flow():
    # create
    res = client.post("/notes", json={
        "notebook_id": "nb1",
        "author_id": "u1",
        "content": "shared note"
    })

    note_id = res.json()["id"]

    # read
    res2 = client.get(f"/notes/{note_id}")

    assert res2.status_code == 200
    assert res2.json()["content"] == "shared note"