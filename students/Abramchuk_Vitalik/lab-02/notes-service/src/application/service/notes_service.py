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