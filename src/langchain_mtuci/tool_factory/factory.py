"""Реализация фабрики инструментов"""

from langchain.tools import BaseTool

from ..session.base import AbstractMtuciSession

from .base import AbstractMtuciToolsFactory

from ..tools import (
    UserInfoTool,
    AttendanceTool,
    ScheduleTool
)
from ..session import MtuciSession

from ..formatters import (
        FormatterType,
        AbstractFormatter,
        FormatterFactory
)

class MtuciToolFactory(AbstractMtuciToolsFactory):
    """Реализация фабрики инструментов

    Attributes:
        session: сеесия для работы с ЛК МТУСИ
    """

    def __init__(
        self,
        login: str,
        password: str,
        format_: FormatterType = FormatterType.JSON
    ):
        self.session: AbstractMtuciSession = MtuciSession(
            login, password
        )
        self.formatter: AbstractFormatter = FormatterFactory().create(format_)

    def create_tools(self) -> list[BaseTool]:
        """Создаёт инструменты"""
        return [
            self.create_user_info_tool(),
            self.create_attendance_tool(),
            self.create_schedule_tool()
        ]

    def create_user_info_tool(self) -> UserInfoTool:
        """Создаёт инструмент для получения
        информации о пользователе"""
        tool = UserInfoTool()
        tool.metadata["factory"] = self
        tool.metadata["formatter"] = self.formatter

        return tool

    def create_attendance_tool(self) -> AttendanceTool:
        """Создаёт инструмент для получения посещаемости"""
        tool = AttendanceTool()
        tool.metadata["factory"] = self
        tool.metadata["formatter"] = self.formatter

        return tool

    def create_schedule_tool(self) -> ScheduleTool:
        """Создаёт инструмент для получения расписания"""
        tool = ScheduleTool()
        tool.metadata["factory"] = self
        tool.metadata["formatter"] = self.formatter

        return tool
