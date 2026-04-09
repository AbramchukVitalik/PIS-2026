from application.query.get_note_by_id_query import GetNoteByIdQuery
from application.query.handlers.get_note_by_id_handler import GetNoteByIdHandler


class FakeRepo:
    def __init__(self):
        self.notes = {}

    def save(self, note):
        self.notes[note.id] = note

    def find_by_id(self, note_id):
        return self.notes.get(note_id)


def test_get_note():
    repo = FakeRepo()
    handler = GetNoteByIdHandler(repo)

    # fake note
    class Note:
        def __init__(self):
            self.id = "1"
            self.title = "T"
            self.content = "C"
            self.history = []

    repo.save(Note())

    result = handler.handle(GetNoteByIdQuery("1"))

    assert result["id"] == "1"
    assert result["title"] == "T"