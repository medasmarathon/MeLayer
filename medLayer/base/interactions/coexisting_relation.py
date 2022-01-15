from medLayer.core.datatype.influencedirection import InfluenceDirection
from medLayer.core.datatype.probability import Probability
from medLayer.core.interface.inode import INode
from medLayer.core.interface.irelation import IRelation


class CoexistingRelation(IRelation):
  probability: Probability

  def __init__(self, coexisting_node: INode, target_node: INode):
    self.fro_node = coexisting_node
    self.to_node = target_node
    super().__init__()

  def with_direction(self, direction: InfluenceDirection):
    self.direction = direction
    return self