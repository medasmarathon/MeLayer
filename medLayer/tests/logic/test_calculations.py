from typing import List
import pytest

from medLayer.base.conceptlayer import ConceptLayer
from medLayer.base.event import Event
from medLayer.base.host import Host
from medLayer.base.logic.calculations import calculate_event_probability, event_observation_status, find_layer_of_event, find_relations_targeting_event
from medLayer.base.observations import Observation


def test_event_observation_status():
  # Arrange
  event1 = Event("1")
  event2 = Event("2")
  event3 = Event("3")
  ob1 = Observation(event1, True)
  ob2 = Observation(event2, False)

  # Assert
  assert event_observation_status(event1, [ob1, ob2]) == True
  assert event_observation_status(event2, [ob1, ob2]) == False
  assert event_observation_status(event3, [ob1, ob2]) == None
  assert event_observation_status(event1, []) == None


def test_find_layer_of_event(
    init_dataset, human_host: Host, symptoms_layer: ConceptLayer, disease_layer: ConceptLayer,
    symptom_events: List[Event], disease_events: List[Event], impossible_event: Event
    ):
  # Assert
  assert find_layer_of_event(human_host, symptom_events[0]) == symptoms_layer
  assert find_layer_of_event(human_host, disease_events[0]) == disease_layer
  assert find_layer_of_event(human_host, impossible_event) == None


def test_find_relations_targeting_event(
    init_dataset_with_relations, human_host: Host, symptom_events: List[Event],
    disease_events: List[Event]
    ):
  assert len(find_relations_targeting_event(disease_events[0], human_host)) == 1
  assert len(find_relations_targeting_event(symptom_events[0], human_host)) == 0


def test_calculate_event_probability__should_return_0(
    init_dataset, human_host: Host, impossible_event: Event
    ):
  assert calculate_event_probability(impossible_event, human_host, []) == 0
  assert calculate_event_probability(
      impossible_event, human_host, [Observation(impossible_event, True)]
      ) == 0


def test_calculate_event_probability__should_return_1(
    init_dataset, human_host: Host, symptom_events: List[Event], disease_events: List[Event]
    ):
  assert calculate_event_probability(
      symptom_events[0], human_host, [Observation(symptom_events[0], True)]
      ) == 1
  assert calculate_event_probability(
      disease_events[0], human_host, [Observation(disease_events[0], True)]
      ) == 1
