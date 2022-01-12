from medLayer.core.datatype.probability import Probability
from medLayer.core.interface.irelation import IRelation


class DefinitiveRelation(IRelation):
  defining_prob: Probability     # probability of an occuring-observed defining event is part of a defined event
  consisting_prob: Probability     # probability of an occuring-observed defined event consists of an occuring defining event
