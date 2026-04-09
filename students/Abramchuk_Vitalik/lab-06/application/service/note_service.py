from application.commands.create_note_command import CreateNoteCommand
from application.handlers.create_note_handler import CreateNoteHandler


class NoteService:
    def __init__(self, repository):
        self.handler = CreateNoteHandler(repository)

    def create(self, notebook_id, author_id, content):
        cmd = CreateNoteCommand(notebook_id, author_id, content)
        return self.handler.handle(cmd)