from fastapi import FastAPI
from infrastructure.repository.in_memory_note_repository import InMemoryNoteRepository
from application.service.note_service import NoteService

app = FastAPI()

repo = InMemoryNoteRepository()
service = NoteService(repo)


@app.post("/notes")
def create_note(req: dict):
    note = service.create(
        req["notebook_id"],
        req["author_id"],
        req["content"]
    )
    return {"id": note.note_id}


@app.get("/notes/{note_id}")
def get_note(note_id: str):
    note = repo.find_by_id(note_id)
    if not note:
        return {"error": "not found"}

    return {
        "id": note.note_id,
        "content": note.content
    }