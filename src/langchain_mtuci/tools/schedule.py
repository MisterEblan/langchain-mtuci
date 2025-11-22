"""Инструмент для полученя расписания на определённую дату"""

from typing import Any, Type
from langchain.tools import BaseTool
from mtuci_private_api import Mtuci
from datetime import datetime

from .inputs import ScheduleInput

class ScheduleTool(BaseTool):
    """Инструмент для полученя расписания на определённую дату"""

    name: str = "mtuci_schedule"
    description: str = "Получает расписание на определённую дату"
    args_schema: Type[ScheduleInput] = ScheduleInput
    metadata: dict[str, Any] = {"factory": None}

    async def _arun(
        self,
        date: str
    ) -> list[dict[str, Any]] | dict[str, Any]:
        if not (factory := self.metadata.get("factory")):
            return {"error": "Не найдена фабрика, породившая инструмент"}

        date_ = datetime.strptime(date, "%d.%m.%Y")
        client: Mtuci = await factory.session.get_client()
        try:
            schedule = await client.get_schedule(date_)

            if not schedule.lessons:
                return {"info": "На сегодня нет занятий"}

            return [l.model_dump() for l in schedule.lessons]

        except Exception as err: # pylint disable=W0718
            return {"error": str(err)}

    def _run(self, date: str):
        raise NotImplementedError("Поддерживается только асинхронный режим")
