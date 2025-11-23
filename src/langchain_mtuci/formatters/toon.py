"""Форматер для TOON"""

from typing import Any
from .base import AbstractFormatter
from .models import MtuciPrivateApiObjects
from toon_python import encode

class ToonFormatter(
    AbstractFormatter[MtuciPrivateApiObjects, str]
):
    """Форматирование в TOON"""

    def format(
        self,
        obj: MtuciPrivateApiObjects,
        **kwargs: Any
    ) -> str:
        """Форматирует модель в TOON

        Args:
            obj: модель из mtuci private api.
            **kwargs: дополнительные параметры.
                Не используются.

        Returns:
            Строка в формате TOON.
        """

        if isinstance(obj, list):
            obj_json = [o.model_dump() for o in obj]
        else:
            obj_json = obj.model_dump()

        encoded = encode(obj_json)

        return encoded

