import pytest
from domain.models.note import Note
from domain.models.tag import Tag
from domain.exceptions.domain_exception import InvariantViolation


def test_cannot_create_empty_note():
    with pytest.raises(InvariantViolation):
        Note("N1", "NB1", "user1", "")


def test_edit_creates_history():
    note = Note("N1", "NB1", "user1", "Hello")
    note.edit("user2", "New content")

    assert len(note._history) == 1


def test_cannot_add_same_tag_twice():
    note = Note("N1", "NB1", "user1", "Hello")
    tag = Tag("work")

    note.add_tag(tag)
    with pytest.raises(InvariantViolation):
        note.add_tag(tag)


def test_max_tags_limit():
    note = Note("N1", "NB1", "user1", "Hello")

    for i in range(10):
        note.add_tag(Tag(f"t{i}"))

    with pytest.raises(InvariantViolation):
        note.add_tag(Tag("overflow"))