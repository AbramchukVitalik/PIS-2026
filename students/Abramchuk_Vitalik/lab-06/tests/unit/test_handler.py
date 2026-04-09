from application.handlers.create_note_handler import CreateNoteHandler
from application.commands.create_note_command import CreateNoteCommand


class FakeRepo:
    def save(self, note):
        return note


def test_handler_creates_note():
    repo = FakeRepo()
    handler = CreateNoteHandler(repo)

    cmd = CreateNoteCommand("1", "1", "text")
    result = handler.handle(cmd)

    assert result.content == "text"