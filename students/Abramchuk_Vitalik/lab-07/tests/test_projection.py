from cqrs.write_model.note import Note
from cqrs.write_model.repository import InMemoryNoteRepository
from cqrs.projection.note_projection import NoteProjection


def test_cqrs_flow():
    repo = InMemoryNoteRepository()
    projection = NoteProjection()

    # CREATE
    note = Note.create("nb1", "u1", "hello")
    repo.save(note)

    for event in note.pull_events():
        projection.handle(event)

    view = projection.get(note.note_id)

    assert view is not None
    assert view.content == "hello"

    # EDIT
    note.edit("u2", "updated")

    for event in note.pull_events():
        projection.handle(event)

    view2 = projection.get(note.note_id)

    assert view2.content == "updated"