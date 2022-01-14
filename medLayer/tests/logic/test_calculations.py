from typing import List
import pytest

from medLayer.base.conceptlayer import ConceptLayer
from medLayer.base.event import Event
from medLayer.base.host import Host


def test_calculate_event_probability(
    human_host: Host, conceptlayer_1: ConceptLayer, conceptlayer_2: ConceptLayer,
    events_for_layer_1: List[Event], events_for_layer_2: List[Event], impossible_event: Event
    ):
  print(impossible_event.name)
  assert impossible_event.name == "Impossible"
