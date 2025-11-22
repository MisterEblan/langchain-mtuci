import pytest

from src.langchain_mtuci.tool_factory.base import AbstractMtuciToolsFactory
from src.langchain_mtuci import AttendanceTool


class TestAttendanceTool:

    @pytest.fixture
    def tool(self, fake_factory: AbstractMtuciToolsFactory) -> AttendanceTool:
        tool = AttendanceTool()

        tool.metadata["factory"] = fake_factory

        return tool

    async def test_arun(
        self,
        tool: AttendanceTool
    ):
        result = await tool.arun({})

        assert result

    async def test_run(
        self,
        tool: AttendanceTool
    ):
        with pytest.raises(NotImplementedError):
            await tool.run({})

    async def test_no_factory(
        self,
        tool: AttendanceTool
    ):
        tool.metadata["factory"] = None

        result = await tool.arun({})

        assert result
        assert result["error"]
