from domain.models.note import Note
from application.command.create_note_command import CreateNoteCommand
from application.port.out.note_repository import NoteRepository


class CreateNoteHandler:
    def __init__(self, repository: NoteRepository):
        self.repository = repository

    def handle(self, command: CreateNoteCommand) -> str:
        note = Note(
            title=command.title,
            content=command.content
        )

        self.repository.save(note)
        return note.id