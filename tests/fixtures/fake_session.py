from langchain.tools import BaseTool
from mtuci_private_api import Mtuci
from src.langchain_mtuci.session.base import AbstractMtuciSession
from .fake_mtuci_client import FakeMtuciClient

import pytest


class FakeSession(AbstractMtuciSession):

    def create_tools(self) -> list[BaseTool]:
        return []

    async def get_client(self) -> Mtuci:
        return FakeMtuciClient()

    async def close(self) -> None:
        return

@pytest.fixture
def fake_session() -> AbstractMtuciSession:
    return FakeSession()
