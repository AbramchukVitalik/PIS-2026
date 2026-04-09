from application.command.edit_note_command import EditNoteCommand
from application.port.out.note_repository import NoteRepository


class EditNoteHandler:
    def __init__(self, repository: NoteRepository):
        self.repository = repository

    def handle(self, command: EditNoteCommand) -> None:
        note = self.repository.find_by_id(command.note_id)

        if not note:
            raise ValueError("Note not found")

        note.edit(
            editor=command.editor,
            new_content=command.new_content
        )

        self.repository.save(note)