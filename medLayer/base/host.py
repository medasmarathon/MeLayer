from typing import MutableMapping
from medLayer.base.event import Event
from medLayer.core.interface import IHost
from probnode.datatype.probabilityvalue import ProbabilityValue


class EventToProbabilityDictionary(MutableMapping):

  def __init__(self, *args, **kwargs):
    self._data = dict()
    self.update(*args, **kwargs)

  def __iter__(self):
    return self._data.__iter__()

  def __setitem__(self, event, probability):
    if not isinstance(probability, ProbabilityValue):
      raise TypeError(repr(type(probability)))
    if not isinstance(event, Event):
      raise TypeError(repr(type(probability)))
    self._data.__setitem__(event, probability)

  def __delitem__(self, key):
    self._data.__delitem__(key)

  def __getitem__(self, key):
    try:
      return self._data.__getitem__(key)
    except KeyError:
      return ProbabilityValue(0)

  def __len__(self):
    return self._data.__len__()


class Host(IHost):
  base_probability_of: EventToProbabilityDictionary = EventToProbabilityDictionary()

  def __init__(self, name: str):
    super().__init__()
    self.name = name
    self.layers = []
    self.interactions = []
