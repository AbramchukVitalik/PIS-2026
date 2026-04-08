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