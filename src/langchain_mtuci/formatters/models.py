"""Модели и типы данных для форматеров"""

from enum import Enum
from typing import Any
from pydantic import BaseModel

type MtuciPrivateApiObjects = BaseModel | list[BaseModel]
type JsonFormatted = dict[str, Any] | list[dict[str, Any]]

class FormatterType(str, Enum):
    """Перечисление возможных форматтеров"""

    JSON = "json"
    TOON = "toon"
