from medLayer.core.datatype.probabilityvalue import ProbabilityValue
from medLayer.core.interface import INode


class Event(INode):
  independent_prob: ProbabilityValue = ProbabilityValue(0)

  def __init__(self, name: str):
    super().__init__()
    self.name = name

  def with_base_prob(self, prob: float):
    self.independent_prob = ProbabilityValue(prob)
    return self

  def __key(self):
    return (self.name)

  def __hash__(self):
    return hash(self.__key())

  def __eq__(self, other: "Event") -> bool:
    if isinstance(other, Event):
      return self.__key() == other.__key()
    raise NotImplementedError
