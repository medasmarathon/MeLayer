from ..core.datatype import InfluenceDirection
from .inode import INode


class IInteraction:
  direction: InfluenceDirection
  fro_node: INode
  to_node: INode
  inherent_value: float
