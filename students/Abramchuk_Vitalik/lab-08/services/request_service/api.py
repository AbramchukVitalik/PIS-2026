# services/request_service/api.py
from fastapi import FastAPI
from infrastructure.repo import InMemoryNoteRepository
from infrastructure.rabbitmq_publisher import RabbitPublisher
from application.create_note_handler import CreateNoteHandler

app = FastAPI()

repo = InMemoryNoteRepository()
publisher = RabbitPublisher()
handler = CreateNoteHandler(repo, publisher)


@app.post("/notes")
def create_note(data: dict):
    note_id = handler.handle(
        data["notebook_id"],
        data["author_id"],
        data["content"]
    )

    return {"id": note_id}


@app.get("/notes/{note_id}")
def get_note(note_id: str):
    return repo.get(note_id)