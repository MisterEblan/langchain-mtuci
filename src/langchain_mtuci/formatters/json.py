"""JSON-Форматтер"""

from typing import Any
from .base import AbstractFormatter
from .models import (
        MtuciPrivateApiObjects,
        JsonFormatted
)

class JsonFormatter(
    AbstractFormatter[MtuciPrivateApiObjects, JsonFormatted]
):
    """Форматирование в JSON"""

    def format(
        self,
        obj: MtuciPrivateApiObjects,
        **kwargs: Any
    ) -> JsonFormatted:
        """Форматирует объект в JSON

        Args:
            obj: объекты из mtuci private api.
            **kwargs: дополнительные параметры.
                Не используются.

        Returns:
            Словарь/список словарей с данными.
        """
        if isinstance(obj, list):
            return [o.model_dump() for o in obj]
        else:
            return obj.model_dump()
