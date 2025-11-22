from langchain.tools import BaseTool
import pytest
from src.langchain_mtuci.tool_factory.base import AbstractMtuciToolsFactory
from .fake_session import FakeSession

class FakeFactory(AbstractMtuciToolsFactory):

    session = FakeSession()

    def create_tools(self) -> list[BaseTool]:
        return []

@pytest.fixture
def fake_factory() -> AbstractMtuciToolsFactory:
    return FakeFactory()
