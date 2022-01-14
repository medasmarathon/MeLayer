from typing import List, Union
from medLayer.base.event import Event
from medLayer.base.host import Host
from medLayer.base.observations import Observation
from medLayer.core.datatype.probability import Probability
from medLayer.core.interface.ilayer import ILayer


def calculate_event_probability(
    event: Event, host: Host, observations: List[Observation]
    ) -> Probability:
  obs_status = event_observation_status(event, observations)
  if obs_status is not None:
    return Probability(obs_status)

  conceptLayer = find_layer_of_event(host, event)
  if conceptLayer is None:
    return Probability(0)
  return Probability(0)


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