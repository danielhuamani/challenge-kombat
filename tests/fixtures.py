import pytest
from app.domain.models import PlayerDomain


@pytest.fixture
def player_tonyn():
    return PlayerDomain(name="Tonyn")


@pytest.fixture
def player_arnaldor():
    return PlayerDomain(name="Arnaldor")
