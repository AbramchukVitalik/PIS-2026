# Лабораторная работа №2. Гексагональная архитектура

**Дисциплина:** Проектирование интернет-систем  
**Тема:** Проектирование архитектуры: порты, адаптеры и изоляция домена

---

> 🚀 **Важно:** Эта лабораторная работа посвящена **архитектурному проектированию**. Мы создаём структуру проекта, интерфейсы портов и минимальные примеры каждого слоя для сервиса "Заметки «Пишем вдвоём»". Детальная реализация будет в Lab #3-5.

---

## Цель работы

Спроектировать архитектуру сервиса **Notes Service** с использованием гексагональной (hexagonal) архитектуры: создать структуру проекта, определить порты (интерфейсы) и продемонстрировать изоляцию слоёв через минимальные примеры.

## Результаты обучения

После выполнения работы студент будет:

- Понимать принципы гексагональной архитектуры (Ports & Adapters)
- Уметь проектировать структуру проекта с разделением на слои: domain, application, infrastructure
- Определять порты (интерфейсы) для входящих и исходящих взаимодействий
- Применять Dependency Inversion Principle (DIP) на уровне проектирования
- Понимать как слои взаимодействуют через интерфейсы

---

## Теоретическая справка

### Гексагональная архитектура (Alistair Cockburn, 2005)

**Идея**: бизнес-логика (домен) изолирована от внешнего мира через порты и адаптеры.

```
        ┌─────────────────────────┐
        │   Внешний мир           │
        │  (UI, БД, API, очереди) │
        └────────────┬────────────┘
                     │
            ┌────────▼────────┐
            │   Адаптеры      │ ◄─── Реализации (HTTP, PostgreSQL)
            │   (Infra Layer) │
            └────────┬────────┘
                     │
            ┌────────▼────────┐
            │     Порты       │ ◄─── Интерфейсы (INotesService, IRepository)
            │  (Application)  │
            └────────┬────────┘
                     │
            ┌────────▼────────┐
            │     Домен       │ ◄─── Чистая бизнес-логика (Note, Notebook, Tag)
            │  (Domain Layer) │
            └─────────────────┘
```

### Слои

1. **Domain** (ядро):
   - Сущности: `Note`, `Notebook`, `Tag`
   - Доменная логика и история изменений
   - **Не зависит** от фреймворков, БД, UI

2. **Application** (прикладной слой):
   - Use-case (сценарии): создание, редактирование, назначение тегов
   - Порты (интерфейсы):
     - **Входящие**: `INotesService` (клиент вызывает систему)
     - **Исходящие**: `INoteRepository`, `INotificationService`

3. **Infrastructure** (инфраструктурный):
   - Адаптеры:
     - **Входящие**: REST контроллеры, WebSocket, GraphQL
     - **Исходящие**: репозитории БД, клиенты внешних сервисов, очередь событий

### Dependency Rule

Зависимости направлены внутрь (к домену):

```
Infrastructure → Application → Domain
     ↓                ↓            ↓
[Controllers]  →  [Ports]  →  [Entities]
[Repositories]
```

Domain **не знает** о Infrastructure.

---

## Задание

### Часть 1. Архитектурная диаграмма

Сервис: **Notes Service** (Заметки «Пишем вдвоём»)

**Сущности Domain Layer:** `Note`, `Notebook`, `Tag`  
**Use-case Application Layer:** `CreateNote`, `EditNote`, `AssignTag`  
**Адаптеры Infrastructure Layer:**

- Входящие: `NoteController` (REST)
- Исходящие: `InMemoryNoteRepository`, `ConsoleNotificationService`

Диаграмма слоёв + потоки данных:

```
[Client UI] ---> [NoteController] ---> [NotesService] ---> [NoteRepository]
                                               |
                                               ---> [NotificationService]
```

Domain **не зависит** от контроллера и репозитория.

---

### Часть 2. Структура проекта (скелет)

```
notes-service/
├── src/
│   ├── domain/
│   │   ├── models/
│   │   │   ├── note.py
│   │   │   ├── notebook.py
│   │   │   └── tag.py
│   │   └── exceptions/
│   │       └── domain_exception.py
│   │
│   ├── application/
│   │   ├── port/
│   │   │   ├── in/
│   │   │   │   ├── create_note_use_case.py
│   │   │   │   └── get_note_use_case.py
│   │   │   └── out/
│   │   │       ├── note_repository.py
│   │   │       └── notification_service.py
│   │   └── service/
│   │       └── notes_service.py
│   │
│   └── infrastructure/
│       ├── adapter/
│       │   ├── in/
│       │   │   └── note_controller.py
│       │   └── out/
│       │       ├── in_memory_note_repository.py
│       │       └── console_notification_service.py
│       └── config/
│           └── dependency_injection.py
├── README.md
└── Architecture.md
```

---

### Часть 3. Интерфейсы портов

#### Входящие порты

```python
# application/port/in/create_note_use_case.py
from abc import ABC, abstractmethod

class CreateNoteCommand:
    """DTO для создания заметки"""
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

class CreateNoteUseCase(ABC):
    """Входящий порт: создание заметки"""
    @abstractmethod
    def create_note(self, command: CreateNoteCommand) -> str:
        """Создает заметку и возвращает её ID"""
        pass
```

```python
# application/port/in/get_note_use_case.py
from abc import ABC, abstractmethod

class GetNoteUseCase(ABC):
    """Входящий порт: получение заметки"""
    @abstractmethod
    def get_note(self, note_id: str):
        """Возвращает объект Note по ID"""
        pass
```

#### Исходящие порты

```python
# application/port/out/note_repository.py
from abc import ABC, abstractmethod

class NoteRepository(ABC):
    """Исходящий порт: репозиторий заметок"""
    @abstractmethod
    def save(self, note):
        pass

    @abstractmethod
    def find_by_id(self, note_id: str):
        pass
```

```python
# application/port/out/notification_service.py
from abc import ABC, abstractmethod

class NotificationService(ABC):
    """Исходящий порт: уведомления"""
    @abstractmethod
    def notify(self, message: str):
        pass
```

---

### Часть 4. Мини-примеры слоёв

#### Domain Layer

```python
# domain/models/note.py
class Note:
    """Доменная модель: заметка"""
    def __init__(self, note_id: str, title: str, content: str):
        self.id = note_id
        self.title = title
        self.content = content
        self.tags = []
```

#### Application Layer

```python
# application/service/notes_service.py
class NotesService:
    """Сервис для работы с заметками"""
    def __init__(self, repository, notification_service):
        self.repository = repository
        self.notification_service = notification_service

    def create_note(self, command):
        """Создать заметку (пустой скелет)"""
        raise NotImplementedError("Будет реализовано в Lab #4")

    def get_note(self, note_id: str):
        """Получить заметку по ID (пустой скелет)"""
        raise NotImplementedError("Будет реализовано в Lab #4")
```

#### Infrastructure Layer

```python
# infrastructure/adapter/out/in_memory_note_repository.py
class InMemoryNoteRepository:
    """Простейший репозиторий заметок в памяти"""
    def __init__(self):
        self.notes = {}

    def save(self, note):
        self.notes[note.id] = note

    def find_by_id(self, note_id: str):
        return self.notes.get(note_id)
```

---

### Часть 5. DI (скелет)

```python
# infrastructure/config/dependency_injection.py
from ..adapter.out.in_memory_note_repository import InMemoryNoteRepository
from ..adapter.out.console_notification_service import ConsoleNotificationService
from ...application.service.notes_service import NotesService

class DependencyContainer:
    """DI контейнер: связывает адаптеры и сервисы"""
    def __init__(self):
        self.note_repository = InMemoryNoteRepository()
        self.notification_service = ConsoleNotificationService()
        self.notes_service = NotesService(
            repository=self.note_repository,
            notification_service=self.notification_service
        )

    def get_notes_service(self):
        return self.notes_service
```

---

## Контрольные вопросы

1. Преимущество hexagonal architecture перед классической трёхслойной?
2. Почему domain не зависит от infrastructure?
3. Что такое Dependency Inversion Principle и как применяется?
4. Зачем создавать интерфейсы для портов с одной реализацией?
5. Как изменится архитектура при переходе с REST на gRPC?
6. В чём разница входящего и исходящего порта?
7. Почему domain-сущности не имеют аннотаций фреймворков?
8. Как обеспечивается тестируемость?
9. Можно ли заменить InMemoryRepository на PostgreSQLRepository без изменения domain и application?
10. В какой слой поместить валидацию входных данных?
