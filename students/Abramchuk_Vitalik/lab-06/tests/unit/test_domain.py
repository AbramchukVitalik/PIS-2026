import pytest
from domain.note import Note


def test_create_note_valid():
    note = Note.create("1", "1", "hello")
    assert note.content == "hello"


def test_empty_note_fails():
    with pytest.raises(ValueError):
        Note.create("1", "1", "")