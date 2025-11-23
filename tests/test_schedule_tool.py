import pytest

from src.langchain_mtuci.formatters.toon import ToonFormatter
from src.langchain_mtuci.formatters.json import JsonFormatter
from src.langchain_mtuci.tool_factory.base import AbstractMtuciToolsFactory
from src.langchain_mtuci import ScheduleTool


class TestScheduleTool:

    @pytest.fixture
    def tool_json(self, fake_factory: AbstractMtuciToolsFactory) -> ScheduleTool:
        tool_json = ScheduleTool()

        tool_json.metadata["factory"] = fake_factory
        tool_json.metadata["formatter"] = JsonFormatter()

        return tool_json

    @pytest.fixture
    def tool_toon(self, fake_factory: AbstractMtuciToolsFactory) -> ScheduleTool:
        tool_toon = ScheduleTool()

        tool_toon.metadata["factory"] = fake_factory
        tool_toon.metadata["formatter"] = ToonFormatter()

        return tool_toon

    async def test_arun_json(
        self,
        tool_json: ScheduleTool
    ):
        result = await tool_json.arun({"date": "21.11.2025"})

        assert result
        assert isinstance(result, dict)

    async def test_arun_toon(
        self,
        tool_toon: ScheduleTool
    ):
        result = await tool_toon.arun({"date": "21.11.2025"})

        assert result
        assert isinstance(result, str)

    async def test_run(
        self,
        tool_json: ScheduleTool,
        tool_toon: ScheduleTool
    ):
        with pytest.raises(NotImplementedError):
            tool_json.run({"date": "21.11.2025"})

        with pytest.raises(NotImplementedError):
            tool_toon.run({"date": "21.11.2025"})

    async def test_no_factory(
        self,
        tool_json: ScheduleTool
    ):
        tool_json.metadata["factory"] = None

        result = await tool_json.arun({"date": "21.11.2025"})

        assert result
        assert result["error"]

    async def test_no_formatter(
        self,
        tool_json: ScheduleTool
    ):
        tool_json.metadata["formatter"] = None

        result = await tool_json.arun({"date": "21.11.2025"})

        assert result
        assert result["error"]
