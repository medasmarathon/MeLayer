from medLayer.interface import INode


class Node(INode):

  def __key(self):
    return (self.name)

  def __hash__(self):
    return hash(self.__key())

  def __eq__(self, other: "Node") -> bool:
    if isinstance(other, Node):
      return self.__key() == other.__key()
    raise NotImplementedError
