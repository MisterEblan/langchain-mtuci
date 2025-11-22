"""Абстрактная фабрика инструментов"""

from abc import ABC, abstractmethod

from langchain.tools import BaseTool

class AbstractMtuciToolsFactory(ABC):
    """Абстрактная фабрика инструментов"""

    @abstractmethod
    def create_tools(self) -> list[BaseTool]: # pragma: no cover
        """Создаёт инструменты"""
        pass
