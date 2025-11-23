from datetime import datetime
from typing import Any
from src.langchain_mtuci.formatters import (
    ToonFormatter,
    JsonFormatter,
    AbstractFormatter
)
from src.langchain_mtuci.formatters.models import (
    MtuciPrivateApiObjects,
    JsonFormatted
)
from mtuci_private_api import Lesson, LessonType, User, Attendance, Schedule
import pytest

class TestFormatters:

    @pytest.fixture
    def toon_formatter(
        self
    ) -> AbstractFormatter[MtuciPrivateApiObjects, str]:
        return ToonFormatter()

    @pytest.fixture
    def json_formatter(
        self
    ) -> AbstractFormatter[MtuciPrivateApiObjects, JsonFormatted]:
        return JsonFormatter()

    @pytest.fixture
    def user_info(self) -> User:
        return User(
            uid="12345",
            name="Иванов Иван",
            department="РиТ",
            course="Второй",
            group="БББ1234",
            speciality="инженер"
        )

    @pytest.fixture
    def attendance(self) -> list[Attendance]:
        return [
            Attendance(
                subject_name="История",
                attendance_percentage=50.0,
                skips=8
            ),
            Attendance(
                subject_name="Высшая математика",
                attendance_percentage=100.0,
                skips=0
            )
        ]


    @pytest.fixture
    def schedule(self) -> Schedule:
        lessons = [
            Lesson(
                name="Высшая математика",
                type_=LessonType.LECTURE,
                is_retake=False,
                teachers=["Преподаватель"],
                audience=["Е-231"],
                start_time=datetime(2025, 11, 12, hour=12, minute=45),
                end_time=datetime(2025, 11, 12, hour=15, minute=10)
            )
        ]

        return Schedule(
            date=datetime(2025, 11, 21),
            lessons=lessons
        )


    def test_toon_format_user_info(
        self,
        toon_formatter: AbstractFormatter[MtuciPrivateApiObjects, str],
        user_info: User
    ):
        formatted = toon_formatter.format(user_info)

        assert formatted, \
        f"Ожидался не пустой объект. Получили {formatted}"

        assert isinstance(formatted, str), \
        f"Ожидался объект str. Получили {type(formatted)}"

    def test_toon_format_attendance(
        self,
        toon_formatter: AbstractFormatter[MtuciPrivateApiObjects, str],
        attendance: list[Attendance]
    ):
        formatted = toon_formatter.format(attendance)

        assert formatted, \
        f"Ожидался не пустой объект. Получили {formatted}"

        assert isinstance(formatted, str), \
        f"Ожидался объект str. Получили {type(formatted)}"

    def test_toon_format_schedule(
        self,
        toon_formatter: AbstractFormatter[MtuciPrivateApiObjects, str],
        schedule: Schedule
    ):
        formatted = toon_formatter.format(schedule)

        assert formatted, \
        f"Ожидался не пустой объект. Получили {formatted}"

        assert isinstance(formatted, str), \
        f"Ожидался объект str. Получили {type(formatted)}"

    def test_json_format_user_info(
        self,
        json_formatter: AbstractFormatter[MtuciPrivateApiObjects, JsonFormatted],
        user_info: User
    ):
        formatted = json_formatter.format(user_info)

        assert formatted, \
        f"Ожидался не пустой объект. Получили {formatted}"

        assert isinstance(formatted, dict), \
        f"Ожидался объект dict. Получили {type(formatted)}"

    def test_json_format_attendance(
        self,
        json_formatter: AbstractFormatter[MtuciPrivateApiObjects, JsonFormatted],
        attendance: list[Attendance]
    ):
        formatted = json_formatter.format(attendance)

        assert formatted, \
        f"Ожидался не пустой объект. Получили {formatted}"

        assert isinstance(formatted, list), \
        f"Ожидался объект list. Получили {type(formatted)}"

    def test_json_format_schedule(
        self,
        json_formatter: AbstractFormatter[MtuciPrivateApiObjects, JsonFormatted],
        schedule: Schedule
    ):
        formatted = json_formatter.format(schedule)

        assert formatted, \
        f"Ожидался не пустой объект. Получили {formatted}"

        assert isinstance(formatted, dict), \
        f"Ожидался объект dict. Получили {type(formatted)}"
