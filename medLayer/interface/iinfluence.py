from ..core.datatype import InfluenceDirection
from inode import INode


class IInfluence:
  direction: InfluenceDirection
  fro_node: INode
  to_node: INode
