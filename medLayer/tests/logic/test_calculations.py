import pytest


def test_calculate_event_probability(
    human_host, conceptlayer_1, conceptlayer_2, events_for_layer_1, events_for_layer_2,
    sample_impossible_event
    ):
  print(sample_impossible_event.name)
  assert sample_impossible_event.name == "Impossible"
