from .inode import INode
from typing import List


class ILayer:
  name: str
  order: int
  nodes: List[INode]

  def __key(self):
    return (self.name)

  def __hash__(self):
    return hash(self.__key())

  def __eq__(self, other) -> bool:
    raise NotImplementedError