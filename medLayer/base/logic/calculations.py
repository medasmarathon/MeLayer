from typing import List, Union
from event import Event
from medLayer.base import conceptlayer
from medLayer.base.host import Host
from medLayer.base.observations import Observation
from medLayer.core.datatype.probability import Probability
from medLayer.core.interface.ilayer import ILayer


def calculate_event_probability(
    event: Event, host: Host, observations: List[Observation]
    ) -> Probability:
  conceptLayer = find_layer_of_event(host, event)
  if conceptLayer is None:
    return 0
  return 0


def find_layer_of_event(host: Host, event: Event) -> Union[ILayer, None]:
  for layer in host.layers:
    try:
      index = layer.nodes.index(event)
      return layer
    except ValueError:
      continue
  return None