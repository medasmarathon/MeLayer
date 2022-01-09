from ..core.datatype import InfluenceDirection
from .inode import INode
from .iinfluence import IInfluence


class IInteraction:
  direction: InfluenceDirection
  fro_node: INode
  to_node: INode
  influence: IInfluence
