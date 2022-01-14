from typing import List
import pytest

from medLayer.base.conceptlayer import ConceptLayer
from medLayer.base.event import Event
from medLayer.base.host import Host


def test_calculate_event_probability(
    human_host: Host, symptoms_layer: ConceptLayer, disease_layer: ConceptLayer,
    symptom_events: List[Event], disease_events: List[Event], impossible_event: Event
    ):
  print(impossible_event.name)
  assert impossible_event.name == "Impossible"
