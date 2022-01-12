from medLayer.core.datatype import InfluenceDirection
from .inode import INode


class IRelation:
  direction: InfluenceDirection
  fro_node: INode
  to_node: INode
