import pytest

from medLayer.base.conceptlayer import ConceptLayer
from medLayer.base.event import Event
from medLayer.base.host import Host


@pytest.fixture(autouse=True)
def human_host():
  return Host("Human")


@pytest.fixture(autouse=True)
def symptoms_layer():
  return ConceptLayer('Symptoms', 1)


@pytest.fixture(autouse=True)
def disease_layer():
  return ConceptLayer('Disease', 2)


@pytest.fixture(autouse=True)
def symptom_events():
  return [Event('Fever'), Event('Abdominal Pain'), Event('Coughing')]


@pytest.fixture(autouse=True)
def disease_events():
  return [Event('Appendicitis'), Event("Flu")]


@pytest.fixture(autouse=True)
def impossible_event():
  return Event('Impossible')