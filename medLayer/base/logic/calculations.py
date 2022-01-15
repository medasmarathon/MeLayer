from typing import Dict, List, TypedDict, Union
from medLayer.base.event import Event
from medLayer.base.host import Host
from medLayer.base.interactions.coexisting_relation import CoexistingRelation
from medLayer.base.observations import Observation
from medLayer.core.datatype.probabilityvalue import ProbabilityValue
from medLayer.core.interface.ilayer import ILayer
from medLayer.core.interface.irelation import IRelation


def calculate_event_probability(
    event: Event, host: Host, observations: List[Observation]
    ) -> ProbabilityValue:
  # check event possible for host
  event_conceptLayer = find_layer_of_event(host, event)
  if event_conceptLayer is None:
    return ProbabilityValue(0)

  # check event has been observed
  obs_status = event_observation_status(event, observations)
  if obs_status is not None:
    return ProbabilityValue(obs_status)

  # find relations targeting events
  event_relations = find_relations_targeting_event(event, host)

  # if no targeting relations -> return base event prob
  if len(event_relations) == 0:
    return event.independent_prob
  return ProbabilityValue(0)


def event_observation_status(event: Event, observations: List[Observation]) -> Union[bool, None]:
  for ob in observations:
    if ob.node == event and ob.is_observed_occuring is not None:
      return ob.is_observed_occuring
  return None


def find_layer_of_event(host: Host, event: Event) -> Union[ILayer, None]:
  for layer in host.layers:
    try:
      index = layer.nodes.index(event)
      return layer
    except ValueError:
      continue
  return None


def find_relations_targeting_event(event: Event, host: Host) -> Union[None, List[IRelation]]:
  relations = []
  for relation in host.interactions:
    if relation.to_node == event:
      relations.append(relation)
    if type(relation) is CoexistingRelation and relation.fro_node == event:
      relations.append(relation)
  return relations