import pytest


def test_calculate_event_probability(
    sample_host, sample_conceptlayers, sample_events, sample_impossible_event
    ):
  print(sample_impossible_event.name)
  assert sample_impossible_event.name == "a"
