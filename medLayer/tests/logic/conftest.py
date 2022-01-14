import pytest

from medLayer.base.conceptlayer import ConceptLayer
from medLayer.base.event import Event
from medLayer.base.host import Host


@pytest.fixture
def human_host():
  return Host("Human")


@pytest.fixture
def symptoms_layer():
  return ConceptLayer('Symptoms', 1)


@pytest.fixture
def disease_layer():
  return ConceptLayer('Disease', 2)


@pytest.fixture
def symptom_events():
  return [Event('Fever'), Event('Pain')]


@pytest.fixture
def disease_events():
  return [Event('FUO')]


@pytest.fixture
def impossible_event():
  return Event('Impossible')