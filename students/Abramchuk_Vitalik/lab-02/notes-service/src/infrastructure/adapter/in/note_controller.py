# infrastructure/adapter/in/note_controller.py
class NoteController:
    """Входящий адаптер: контроллер заметок"""
    def __init__(self, notes_service):
        self.notes_service = notes_service

    def create_note_endpoint(self, title: str, content: str):
        """Пример метода для эндпоинта"""
        command = type('CreateNoteCommand', (), {'title': title, 'content': content})()
        return self.notes_service.create_note(command)