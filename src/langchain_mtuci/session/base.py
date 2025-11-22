"""Сессия для работы с MTUCI API"""

from mtuci_private_api import Mtuci
from abc import ABC, abstractmethod

class AbstractMtuciSession(ABC):
    """Абстрактная сессия для работы с MTUCI API"""

    @abstractmethod
    async def get_client(self) -> Mtuci: # pragma: no cover
        """Получает клиент для работы с ЛК МТУСИ"""

    @abstractmethod
    async def close(self) -> None: # pragma: no cover
        """Закрывает соединение"""
        pass

class MtuciSession(AbstractMtuciSession):
    """Сессия для работы с MTUCI API

    Attributes:
        login: логин пользователя.
        password: пароль пользователя.
        _client: класс для работы с ЛК МТУСИ.
    """

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self._client: Mtuci | None = None

    async def get_client(self) -> Mtuci:
        """Получает или создает клиент

        Returns:
            Класс для работы с ЛК МТУСИ.
        """
        if self._client is None:
            self._client = await Mtuci( # pylint disable=C2801
                login=self.login,
                password=self.password
            ).__aenter__()
        return self._client

    async def close(self) -> None:
        """Закрывает соединение"""
        if self._client:
            await self._client.__aexit__(None, None, None)
            self._client = None
