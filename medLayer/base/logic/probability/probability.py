from typing import List
from medLayer.base.event import Event
from medLayer.base.interactions.coexisting_relation import CoexistingRelation
from medLayer.base.observations import Observation
from medLayer.core.datatype.probabilityvalue import ProbabilityValue


class IProbExpression:
  computed_event: Event

  def compute(self):
    raise NotImplementedError


class IProbability:
  value: ProbabilityValue


class CompoundEventNaming:

  @classmethod
  def AND(cls, event_A: Event, event_B: Event) -> str:
    return f"{event_A.name} AND {event_B.name}"

  @classmethod
  def OR(self, event_A: Event, event_B: Event) -> str:
    return f"{event_A.name} OR {event_B.name}"

  @classmethod
  def NOT(self, event_A: Event) -> str:
    return f"NOT {event_A.name}"


class Probability(IProbability):

  @classmethod
  def from_probability_expression(cls, prob_expression: IProbExpression):
    return prob_expression.compute()

  def __init__(self, event: Event):
    self.value = event.independent_prob


class ProbabilityExpression(IProbExpression):
  event_list: List[Event]
  numerator: IProbExpression
  denominator: IProbExpression

  def provide(self, event_list: List[Event]) -> IProbExpression:
    self.event_list = event_list
    return self

  def exist(self, event: Event) -> IProbExpression:
    self.computed_event = event
    return self

  def not_exist(self, event: Event) -> IProbExpression:
    self.computed_event = Event(f"Not {event.name}").with_base_prob(1 - event.independent_prob)
    return self

  def both(self, event_A: Event, event_B: Event) -> IProbExpression:
    for eve in self.event_list:
      if eve.name == CompoundEventNaming.AND(event_A, event_B):
        self.computed_event = eve
        return self

    self.computed_event = Event(CompoundEventNaming.AND(event_A, event_B)).with_base_prob(
        event_A.independent_prob * event_B.independent_prob
        )
    return self
