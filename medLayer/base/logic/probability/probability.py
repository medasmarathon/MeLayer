from typing import List
from medLayer.base.event import Event
from medLayer.base.interactions.coexisting_relation import CoexistingRelation
from medLayer.base.observations import Observation
from medLayer.core.datatype.probabilityvalue import ProbabilityValue


def P(event: Event) -> ProbabilityValue:
  return event.independent_prob


def P_pure(event: Event, observations: List[Observation]) -> ProbabilityValue:
  # return independent prob if not observed
  if event.independent_prob == 0 or event.independent_prob == 1:     # if prob is certain (not/ do occur) -> return status
    return event.independent_prob
  # else check if event is observed
  for ob in observations:
    if ob.node == event and ob.is_observed_occuring is not None:
      return ProbabilityValue(ob.is_observed_occuring)
  return event.independent_prob


def P_with_coexisting_relations(
    event: Event, observations: List[Observation], coexisting_relations: List[CoexistingRelation]
    ) -> ProbabilityValue:
  # if event is observed => return status
  if P_pure(event, observations) != event.independent_prob:
    return P_pure(event, observations)
  # else
  for ob in observations:
    for rel in coexisting_relations:
      if ob.node == rel.to_node or ob.node == rel.fro_node:
        print("Has relation --> do calculations")
  return P(event)