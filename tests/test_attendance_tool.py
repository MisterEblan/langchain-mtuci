import pytest

from langchain_mtuci.formatters.toon import ToonFormatter
from src.langchain_mtuci.formatters.json import JsonFormatter
from src.langchain_mtuci.tool_factory.base import AbstractMtuciToolsFactory
from src.langchain_mtuci import AttendanceTool


class TestAttendanceTool:

    @pytest.fixture
    def tool_json(self, fake_factory: AbstractMtuciToolsFactory) -> AttendanceTool:
        tool_json = AttendanceTool()

        tool_json.metadata["factory"] = fake_factory
        tool_json.metadata["formatter"] = JsonFormatter()

        return tool_json

    @pytest.fixture
    def tool_toon(self, fake_factory: AbstractMtuciToolsFactory) -> AttendanceTool:
        tool_toon = AttendanceTool()

        tool_toon.metadata["factory"] = fake_factory
        tool_toon.metadata["formatter"] = ToonFormatter()

        return tool_toon

    async def test_arun_json(
        self,
        tool_json: AttendanceTool
    ):
        result = await tool_json.arun({})

        assert result
        assert isinstance(result, list)

    async def test_arun_toon(
        self,
        tool_toon: AttendanceTool
    ):
        result = await tool_toon.arun({})

        assert result
        assert isinstance(result, str)

    async def test_run(
        self,
        tool_json: AttendanceTool,
        tool_toon: AttendanceTool
    ):
        with pytest.raises(NotImplementedError):
            tool_json.run({})
        
        with pytest.raises(NotImplementedError):
            tool_toon.run({})

    async def test_no_factory(
        self,
        tool_json: AttendanceTool
    ):
        tool_json.metadata["factory"] = None

        result = await tool_json.arun({})

        assert result
        assert result["error"]

    async def test_no_formatter(
        self,
        tool_json: AttendanceTool
    ):
        tool_json.metadata["formatter"] = None

        result = await tool_json.arun({})

        assert result
        assert result["error"]
