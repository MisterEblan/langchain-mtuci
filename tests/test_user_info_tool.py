from langchain_mtuci.tool_factory.base import AbstractMtuciToolsFactory
from src.langchain_mtuci.tools.user_info import UserInfoTool

import pytest


class TestUserInfoTool:

    @pytest.fixture
    def tool(self, fake_factory: AbstractMtuciToolsFactory) -> UserInfoTool:
        tool = UserInfoTool()

        tool.metadata["factory"] = fake_factory

        return tool

    async def test_arun(
        self,
        tool: UserInfoTool
    ):
        result = await tool.arun({})

        assert result

    async def test_run(
        self,
        tool: UserInfoTool
    ):
        with pytest.raises(NotImplementedError):
            await tool.run({})

    async def test_no_factory(
        self,
        tool: UserInfoTool
    ):
        tool.metadata["factory"] = None

        result = await tool.arun({})

        assert result
        assert result["error"]
