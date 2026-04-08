# application/port/in/get_note_use_case.py
from abc import ABC, abstractmethod

class GetNoteUseCase(ABC):
    """Входящий порт: получение заметки"""
    @abstractmethod
    def get_note(self, note_id: str):
        """Возвращает объект Note по ID"""
        pass