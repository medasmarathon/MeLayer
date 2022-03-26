from medLayer.core.datatype.probabilityvalue import ProbabilityValue
from medLayer.core.interface import INode
from probnode import Event as GenericEvent


class Event(GenericEvent):

  def __hash__(self) -> int:
    return hash(repr(self))
