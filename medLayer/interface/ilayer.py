from inode import INode
from typing import List


class ILayer:
  order: int
  nodes: List[INode]