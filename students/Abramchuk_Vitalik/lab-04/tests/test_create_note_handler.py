import pytest

from application.command.create_note_command import CreateNoteCommand
from application.command.handlers.create_note_handler import CreateNoteHandler


class FakeRepo:
    def __init__(self):
        self.data = {}

    def save(self, note):
        self.data[note.id] = note

    def find_by_id(self, note_id):
        return self.data.get(note_id)


def test_create_note_handler():
    repo = FakeRepo()
    handler = CreateNoteHandler(repo)

    command = CreateNoteCommand(
        title="Test",
        content="Hello world"
    )

    note_id = handler.handle(command)

    assert note_id is not None
    assert note_id in repo.data