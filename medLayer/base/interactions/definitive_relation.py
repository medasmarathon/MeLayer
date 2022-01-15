from medLayer.core.datatype.influencedirection import InfluenceDirection
from medLayer.core.datatype.probability import Probability
from medLayer.core.interface.inode import INode
from medLayer.core.interface.irelation import IRelation


class DefinitiveRelation(IRelation):
  defining_prob: Probability     # probability of an occuring-observed defining event is part of a defined event
  consisting_prob: Probability     # probability of an occuring-observed defined event consists of an occuring defining event

  def __init__(
      self,
      defining_node: INode,
      target_node: INode,
      defining_prob: Probability = None,
      consisting_prob: Probability = None
      ):
    self.fro_node = defining_node
    self.to_node = target_node
    self.defining_prob = defining_prob
    self.consisting_prob = consisting_prob
    super().__init__()

  def with_direction(self, direction: InfluenceDirection):
    self.direction = direction
    return self