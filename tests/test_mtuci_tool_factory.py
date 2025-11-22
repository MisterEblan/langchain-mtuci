from langchain.tools import BaseTool
from mtuci_private_api.mtuci.base import AbstractMtuci
import pytest
from src.langchain_mtuci import MtuciToolFactory

class TestMtuciToolFactory:

    @pytest.fixture
    def factory(
        self,
        login: str,
        password: str,
        fake_mtuci: AbstractMtuci
    ) -> MtuciToolFactory:
        factory = MtuciToolFactory(login, password)
        factory.session._client = fake_mtuci

        return factory

    def test_get_tools(
        self,
        factory: MtuciToolFactory
    ):
        tools = factory.create_tools()

        assert tools, \
        f"Ожидался не пустой ответ. Получили {tools}"

        assert all(
            isinstance(t, BaseTool)
            for t in tools
        ), "Ожидалось, что все элементы будут наследоваться от BaseTool"

    async def test_user_info(
        self,
        factory: MtuciToolFactory
    ):
        user_tool = factory.create_user_info_tool()

        result = await user_tool.arun({})

        print(result)

        assert result, \
        f"Ожидался не пустой ответ. Получили {result}"

    async def test_attendance(
        self,
        factory: MtuciToolFactory
    ):
        attendance_tool = factory.create_attendance_tool()

        result = await attendance_tool.arun({})
        print(result)

        assert result, \
        f"Ожидался не пустой ответ. Получили {result}"

    async def test_schedule(
        self,
        factory: MtuciToolFactory
    ):
        schedule_tool = factory.create_schedule_tool()

        result = await schedule_tool.arun({"date": "21.11.2025"})
        print(result)

        assert result, \
        f"Ожидался не пустой ответ. Получили {result}"
