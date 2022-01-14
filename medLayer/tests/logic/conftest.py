import pytest

from medLayer.base.conceptlayer import ConceptLayer
from medLayer.base.event import Event
from medLayer.base.host import Host


@pytest.fixture
def human_host():
  return Host("Human")


@pytest.fixture
def conceptlayer_1():
  return ConceptLayer('Symptoms', 1)


@pytest.fixture
def conceptlayer_2():
  return ConceptLayer('Disease', 2)


@pytest.fixture
def events_for_layer_1():
  return [Event('Fever'), Event('Pain')]


@pytest.fixture
def events_for_layer_2():
  return [Event('FUO')]


@pytest.fixture
def sample_impossible_event():
  return Event('Impossible')