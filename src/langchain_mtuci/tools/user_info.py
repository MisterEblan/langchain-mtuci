"""Инструмент для получения информации о пользователе"""

from typing import Any
from langchain.tools import BaseTool
from mtuci_private_api import Mtuci

class UserInfoTool(BaseTool):
    """Инструмент для получения информации о пользователе"""
    name: str = "mtuci_user_info"
    description: str = (
        "Получает информацию о пользователе личного кабинета МТУСИ."
    )
    metadata: dict[str, Any] = {"factory": None}

    async def _arun(self) -> dict[str, Any]:
        if not (factory := self.metadata.get("factory")):
            return {"error": "Не найдена фабрика, породившая инструмент"}
        client: Mtuci = await factory.session.get_client()
        user_info = await client.get_user_info()

        return user_info.model_dump()

    def _run(self):
        raise NotImplementedError("Поддерживается только асинхронный режим")
