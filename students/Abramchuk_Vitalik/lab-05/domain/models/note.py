from datetime import datetime
from typing import List

from domain.models.tag import Tag
from domain.models.note_history_entry import NoteHistoryEntry
from domain.models.note_status import NoteStatus
from domain.events.note_events import NoteCreated, NoteEdited, TagAddedToNote
from domain.exceptions.domain_exception import InvariantViolation


class Note:
    """
    Aggregate Root: Заметка
    Управляет:
      - содержимым
      - историей изменений
      - метками
    """

    MAX_TAGS = 10
    MAX_HISTORY = 50

    def __init__(self, note_id: str, notebook_id: str, author_id: str, content: str):
        self.note_id = note_id
        self.notebook_id = notebook_id
        self.author_id = author_id
        self.content = content

    # ------------------ Бизнес-методы ------------------

    def edit(self, editor_id: str, new_content: str):
        if self._status == NoteStatus.ARCHIVED:
            raise InvariantViolation("Cannot edit archived note")

        if not new_content.strip():
            raise InvariantViolation("Content cannot be empty")

        # сохраняем историю
        self._history.append(
            NoteHistoryEntry(
                editor_id=editor_id,
                content_snapshot=self._content,
                edited_at=datetime.now()
            )
        )

        if len(self._history) > self.MAX_HISTORY:
            self._history.pop(0)

        self._content = new_content
        self._status = NoteStatus.ACTIVE

        self._register_event(NoteEdited(
            note_id=self._id,
            editor_id=editor_id,
            occurred_at=datetime.now()
        ))

    def add_tag(self, tag: Tag):
        if len(self._tags) >= self.MAX_TAGS:
            raise InvariantViolation("Maximum number of tags reached")

        if tag in self._tags:
            raise InvariantViolation("Tag already added")

        self._tags.append(tag)

        self._register_event(TagAddedToNote(
            note_id=self._id,
            tag_name=tag.name,
            occurred_at=datetime.now()
        ))

    def archive(self):
        self._status = NoteStatus.ARCHIVED

    # ------------------ Events ------------------

    def _register_event(self, event):
        self._events.append(event)

    def pull_events(self):
        events = self._events[:]
        self._events.clear()
        return events

    # ------------------ Equality ------------------

    def __eq__(self, other):
        return isinstance(other, Note) and self._id == other._id

    def __hash__(self):
        return hash(self._id)