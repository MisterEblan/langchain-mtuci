"""Абстрактный форматер"""

from abc import ABC, abstractmethod
from typing import Any

class AbstractFormatter[T, P](ABC):
    """Абстрактный форматер"""

    @abstractmethod
    def format(
        self,
        obj: T,
        **kwargs: Any
    ) -> P:
        """Форматерует объект

        Args:
            obj: объект, который нужно отформатировать.
            **kwargs: дополнительные параметры.

        Returns:
            Отформатированный объект.
        """
