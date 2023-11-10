import pytest

from commons.util import clear_yaml


@pytest.fixture(scope='session', autouse=True)
def clear_start():
    clear_yaml()
    yield 