from application.command.create_note_command import CreateNoteCommand
from application.command.edit_note_command import EditNoteCommand
from application.command.handlers.create_note_handler import CreateNoteHandler
from application.command.handlers.edit_note_handler import EditNoteHandler

from application.query.get_note_by_id_query import GetNoteByIdQuery
from application.query.handlers.get_note_by_id_handler import GetNoteByIdHandler


class NoteService:
    """
    Фасад Application Layer (CQRS)
    Делегирует команды и запросы в handlers
    """

    def __init__(self, repository):
        self.create_handler = CreateNoteHandler(repository)
        self.edit_handler = EditNoteHandler(repository)
        self.get_handler = GetNoteByIdHandler(repository)

    # COMMANDS

    def create_note(self, command: CreateNoteCommand) -> str:
        return self.create_handler.handle(command)

    def edit_note(self, command: EditNoteCommand) -> None:
        self.edit_handler.handle(command)

    # QUERIES

    def get_note_by_id(self, query: GetNoteByIdQuery):
        return self.get_handler.handle(query)