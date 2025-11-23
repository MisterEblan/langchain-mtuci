from src.langchain_mtuci.tool_factory.base import AbstractMtuciToolsFactory
from src.langchain_mtuci.tools.user_info import UserInfoTool
from src.langchain_mtuci.formatters import JsonFormatter, ToonFormatter

import pytest


class TestUserInfoTool:

    @pytest.fixture
    def tool_json(self, fake_factory: AbstractMtuciToolsFactory) -> UserInfoTool:
        tool = UserInfoTool()

        tool.metadata["factory"] = fake_factory
        tool.metadata["formatter"] = JsonFormatter()

        return tool

    @pytest.fixture
    def tool_toon(self, fake_factory: AbstractMtuciToolsFactory) -> UserInfoTool:
        tool = UserInfoTool()

        tool.metadata["factory"] = fake_factory
        tool.metadata["formatter"] = ToonFormatter()

        return tool

    async def test_arun_json(
        self,
        tool_json: UserInfoTool
    ):
        result = await tool_json.arun({})

        assert result
        assert isinstance(result, dict)

    async def test_arun_toon(
        self,
        tool_toon: UserInfoTool
    ):
        result = await tool_toon.arun({})

        assert result
        assert isinstance(result, str)

    async def test_run(
        self,
        tool_json: UserInfoTool,
        tool_toon: UserInfoTool
    ):
        with pytest.raises(NotImplementedError):
            tool_json.run({})

        with pytest.raises(NotImplementedError):
            tool_toon.run({})

    async def test_no_factory(
        self,
        tool_json: UserInfoTool
    ):
        tool_json.metadata["factory"] = None

        result = await tool_json.arun({})

        assert result
        assert result["error"]

    async def test_no_formatter(
        self,
        tool_json: UserInfoTool
    ):
        tool_json.metadata["formatter"] = None

        result = await tool_json.arun({})

        assert result
        assert result["error"]
