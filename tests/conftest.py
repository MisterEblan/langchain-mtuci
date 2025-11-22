from dotenv import load_dotenv
from os import getenv
from .fixtures.fake_mtuci_client import fake_mtuci
from .fixtures.fake_factory import fake_factory
from .fixtures.fake_session import fake_session

import pytest

load_dotenv()

@pytest.fixture
def login() -> str:
    return getenv("MTUCI_LOGIN", "")

@pytest.fixture
def password() -> str:
    return getenv("MTUCI_PASSWORD", "")

