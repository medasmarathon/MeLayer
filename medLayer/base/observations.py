from typing import Union
from medLayer.base.event import Event
from medLayer.core.interface.iobservation import IObservation


class Observation(IObservation):
  is_observed_occuring: Union[bool, None]

  def __init__(self, event: Event, status: Union[bool, None] = None):
    super().__init__()
    self.node = event
    self.is_observed_occuring = status
