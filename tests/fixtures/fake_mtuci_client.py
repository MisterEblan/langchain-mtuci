from datetime import datetime
from typing import Any
from mtuci_private_api import Mtuci
from mtuci_private_api.models import Attendance, Lesson, LessonType, Schedule, User

import pytest

class FakeMtuciClient(Mtuci):
    
    def __init__(self):
        pass

    async def auth(self, **kwargs: Any) -> None:
        return

    async def get_user_info(self, **kwargs: Any) -> User:
        return User(
            uid="12345",
            name="Иванов Иван",
            department="РиТ",
            course="Второй",
            group="БББ1234",
            speciality="инженер"
        )

    async def get_attendace(self, **kwargs: Any) -> list[Attendance]:
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

    async def get_schedule(
        self,
        date: datetime,
        **kwargs: Any
    ) -> Schedule:

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
            date=date,
            lessons=lessons
        )

@pytest.fixture
def fake_mtuci() -> Mtuci:
    return FakeMtuciClient()
