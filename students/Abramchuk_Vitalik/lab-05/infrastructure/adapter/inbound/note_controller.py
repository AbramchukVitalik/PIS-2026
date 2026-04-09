from fastapi import FastAPI
from application.command.create_note_command import CreateNoteCommand
from application.service.note_service import NoteService
from infrastructure.adapter.outbound.in_memory_note_repository import InMemoryNoteRepository

app = FastAPI()

# DI (важно!)
repository = InMemoryNoteRepository()
service = NoteService(repository)


@app.post("/notes")
def create_note(data: dict):
    command = CreateNoteCommand(
        notebook_id=data["notebook_id"],
        author_id=data["author_id"],
        content=data["content"]
    )

    note_id = service.create_note(command)
    return {"id": note_id}


@app.get("/notes/{note_id}")
def get_note(note_id: str):
    note = service.get_note(note_id)
    return {
        "id": note.note_id,
        "content": note.content
    }