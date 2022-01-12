from .inode import INode
from typing import List


class ILayer:
  name: str
  order: int
  nodes: List[INode]