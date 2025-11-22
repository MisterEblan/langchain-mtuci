"""Инструмент для получения информации о посещаемости"""

from typing import Any
from langchain.tools import BaseTool
from mtuci_private_api import Mtuci

class AttendanceTool(BaseTool):
    """Инструмент для получения информации о посещаемости"""

    name: str = "mtuci_attendance"
    description: str = "Получает информацию о посещаемости по предметам."
    metadata: dict[str, Any] = {"factory": None}

    async def _arun(self) -> list[dict] | dict[str, str]:
        if not (factory := self.metadata.get("factory")):
            return {"error": "Не найдена фабрика, породившая инструмент"}
        client: Mtuci = await factory.session.get_client()
        attendance = await client.get_attendace()

        return [a.model_dump(exclude={"uid"}) for a in attendance]

    def _run(self):
        raise NotImplementedError("Поддерживается только асинхронный режим")
