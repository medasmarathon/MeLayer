from typing import Union
from medLayer.core.interface.iobservation import IObservation


class Observation(IObservation):
  is_observed_occuring: Union[bool, None]
