from medLayer.core.datatype.probability import Probability
from medLayer.core.interface import INode


class Event(INode):
  independent_prob: Probability

  def __key(self):
    return (self.name)

  def __hash__(self):
    return hash(self.__key())

  def __eq__(self, other: "Event") -> bool:
    if isinstance(other, Event):
      return self.__key() == other.__key()
    raise NotImplementedError
