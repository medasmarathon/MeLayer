from typing import List
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


@pytest.fixture
def add_layers_to_host(human_host: Host, symptoms_layer: ConceptLayer, disease_layer: ConceptLayer):
  human_host.layers = [symptoms_layer, disease_layer]


@pytest.fixture
def add_events_to_layers(
    symptoms_layer: ConceptLayer, disease_layer: ConceptLayer, symptom_events: List[Event],
    disease_events: List[Event]
    ):
  symptoms_layer.nodes = symptom_events
  disease_layer.nodes = disease_events


@pytest.fixture
def init_dataset(add_layers_to_host, add_events_to_layers):
  pass