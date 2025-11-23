"""Абстрактная фабрика форматеров"""

from abc import ABC, abstractmethod

from ..base import AbstractFormatter
from ..models import FormatterType
from ..json import JsonFormatter
from ..toon import ToonFormatter

class AbstractFormatterFactory(ABC):
    """Абстрактная фабрика форматтеров"""

    @abstractmethod
    def create(
        self,
        type_: FormatterType
    ) -> AbstractFormatter:
        """Создаёт форматер определённого типа

        Args:
            type_: тип форматера.

        Returns:
            Форматер.
        """

class FormatterFactory(AbstractFormatterFactory):
    """Реализация фабрики форматеров"""

    def create(
        self,
        type_: FormatterType
    ) -> AbstractFormatter:
        """Создаёт форматер определённого типа"""
        match type_:
            case FormatterType.JSON:
                return JsonFormatter()
            case FormatterType.TOON:
                return ToonFormatter()
