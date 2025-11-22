"""Модели входных данных инструментов"""

from pydantic import BaseModel, Field

class ScheduleInput(BaseModel):
    """Входные данные для инструмента получения расписания"""
    date: str = Field(description="Дата в формате %d.%m.%Y")
