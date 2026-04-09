# Лабораторная работа №3. Доменный уровень

**Дисциплина:** Проектирование интернет-систем  
**Тема:** Сущности, Value Objects, агрегаты и инварианты  
**Вариант:** 16 (Заметки «Пишем вдвоём»)

---

## 1. Сущности (Entities)

### Notebook (Тетрадь)

```python
class Notebook:
    """Entity: Тетрадь"""
    def __init__(self, notebook_id: str, owner_id: str):
        self._id = notebook_id
        self._owner_id = owner_id
        self._notes: list[Note] = []
        self._collaborators: set[str] = set()

    def add_note(self, note: 'Note'):
        self._notes.append(note)

    def add_collaborator(self, user_id: str):
        self._collaborators.add(user_id)

    @property
    def id(self) -> str:
        return self._id

    def __eq__(self, other):
        return isinstance(other, Notebook) and self._id == other._id

    def __hash__(self):
        return hash(self._id)
```

### Note (Заметка)

```python
from datetime import datetime

class Note:
    """Entity: Заметка"""
    def __init__(self, note_id: str, title: str, content: str):
        self._id = note_id
        self.title = title
        self.content = content
        self.tags: set[Tag] = set()
        self.history: list[NoteHistoryEntry] = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def edit_content(self, new_content: str):
        self.history.append(NoteHistoryEntry(self.content, datetime.now()))
        self.content = new_content
        self.updated_at = datetime.now()

    def add_tag(self, tag: 'Tag'):
        self.tags.add(tag)

    @property
    def id(self) -> str:
        return self._id

    def __eq__(self, other):
        return isinstance(other, Note) and self._id == other._id

    def __hash__(self):
        return hash(self._id)
```

### Tag (Метка)

```python
@dataclass(frozen=True)
class Tag:
    name: str
```

### NoteHistoryEntry (История изменений)

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class NoteHistoryEntry:
    content_snapshot: str
    edited_at: datetime
```

## 2. Value Objects (VOs)

### PhoneNumber

```python
@dataclass(frozen=True)
class PhoneNumber:
    number: str

    def __post_init__(self):
        if not self.number.startswith('+') or not self.number[1:].isdigit():
            raise ValueError('Invalid phone number')
```

### Location

```python
@dataclass(frozen=True)
class Location:
    lat: float
    lon: float

    def __post_init__(self):
        if not (-90 <= self.lat <= 90) or not (-180 <= self.lon <= 180):
            raise ValueError('Invalid coordinates')
```

### NotebookName

```python
@dataclass(frozen=True)
class NotebookName:
    name: str

    def __post_init__(self):
        if not self.name:
            raise ValueError('Notebook name cannot be empty')
```

### NoteTitle

```python
@dataclass(frozen=True)
class NoteTitle:
    title: str

    def __post_init__(self):
        if not self.title:
            raise ValueError('Note title cannot be empty')
```

## 3. Агрегаты

### NotebookAggregate

- Корень агрегата: `Notebook`
- Включает: `Note`, `Tag`, `NoteHistoryEntry`
- Границы агрегата: все заметки и их история живут только внутри Notebook

Инварианты:
| Инвариант | Проверка | Исключение |
|-----------|----------|------------|
| Тетрадь не может быть без заметок при публикации | `if not self._notes` | `ValueError` |
| Заметка не может быть пустой | `if not note.content` | `ValueError` |
| Дубликаты тегов запрещены | `if tag in note.tags` | `ValueError` |

Методы агрегата:

```python
class NotebookAggregate:
    def __init__(self, notebook: Notebook):
        self._notebook = notebook
        self._events: list[DomainEvent] = []

    def add_note_to_notebook(self, note: Note):
        if not note.content:
            raise ValueError('Note cannot be empty')
        self._notebook.add_note(note)
        self._events.append(NoteAddedToNotebook(note.id, self._notebook.id, datetime.now()))
```

## 4. Доменные события

```python
class DomainEvent:
    occurred_at: datetime

@dataclass(frozen=True)
class NoteAddedToNotebook(DomainEvent):
    note_id: str
    notebook_id: str
    occurred_at: datetime

@dataclass(frozen=True)
class NoteEdited(DomainEvent):
    note_id: str
    notebook_id: str
    occurred_at: datetime
```

## 5. Юнит-тесты инвариантов

```python
import pytest

def test_cannot_add_empty_note():
    notebook = Notebook('NB-01', 'U-01')
    note = Note('N-01', 'Test', '')
    aggregate = NotebookAggregate(notebook)

    with pytest.raises(ValueError):
        aggregate.add_note_to_notebook(note)
```

---

Файл содержит сущности, value objects, агрегаты, инварианты, доменные события и пример юнит-теста для Варианта 16 (Заметки «Пишем вдвоём»).
