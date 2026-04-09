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