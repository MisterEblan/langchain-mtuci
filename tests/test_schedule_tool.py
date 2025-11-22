import pytest

from src.langchain_mtuci.tool_factory.base import AbstractMtuciToolsFactory
from src.langchain_mtuci import ScheduleTool


class TestScheduleTool:

    @pytest.fixture
    def tool(self, fake_factory: AbstractMtuciToolsFactory) -> ScheduleTool:
        tool = ScheduleTool()

        tool.metadata["factory"] = fake_factory

        return tool

    async def test_arun(
        self,
        tool: ScheduleTool
    ):
        result = await tool.arun({"date": "21.11.2025"})

        assert result

    async def test_run(
        self,
        tool: ScheduleTool
    ):
        with pytest.raises(NotImplementedError):
            await tool.run({"date": "21.11.2025"})

    async def test_no_factory(
        self,
        tool: ScheduleTool
    ):
        tool.metadata["factory"] = None

        result = await tool.arun({"date": "21.11.2025"})

        assert result
        assert result["error"]
