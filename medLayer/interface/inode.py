class INode:
  name: str

  def __key(self):
    return (self.name)

  def __hash__(self):
    return hash(self.__key())

  def __eq__(self, other: "INode") -> bool:
    if isinstance(other, INode):
      return self.__key() == other.__key()
    return NotImplementedError
