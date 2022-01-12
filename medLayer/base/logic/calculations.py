from typing import List
from conceptlayer import ConceptLayer
from event import Event
from medLayer.base.observations import Observation
from medLayer.core.datatype.probability import Probability


def calculate_event_probability(
    event: Event, layer: ConceptLayer, observations: List[Observation]
    ) -> Probability:
  return 0