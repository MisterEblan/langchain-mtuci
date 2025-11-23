"""Инструмент для получения информации о посещаемости"""

from typing import Any
from langchain.tools import BaseTool
from mtuci_private_api import Mtuci

class AttendanceTool(BaseTool):
    """Инструмент для получения информации о посещаемости"""

    name: str = "mtuci_attendance"
    description: str = "Получает информацию о посещаемости по предметам."
    metadata: dict[str, Any] = {
        "factory": None,
        "formatter": None
    }

    async def _arun(self) -> Any | dict[str, str]:
        if not (factory := self.metadata.get("factory")):
            return {"error": "Не найдена фабрика, породившая инструмент"}

        if not (formatter := self.metadata.get("formatter")):
            return {"error": "Не найден форматер"}

        client: Mtuci = await factory.session.get_client()
        try:
            attendance = await client.get_attendace()

            return formatter.format(attendance)
        except Exception as err: # pylint: disable=W0718
            return {"error": str(err)}

    def _run(self):
        raise NotImplementedError("Поддерживается только асинхронный режим")
