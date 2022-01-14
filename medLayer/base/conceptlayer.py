from medLayer.core.interface.ilayer import ILayer


class ConceptLayer(ILayer):

  def __init__(self, name: str, order: int):
    super().__init__()
    self.name = name
    self.order = order
    self.nodes = []

  def __key(self):
    return (self.name)

  def __hash__(self):
    return hash(self.__key())

  def __eq__(self, other: "ConceptLayer") -> bool:
    if isinstance(other, ConceptLayer):
      return self.__key() == other.__key()
    raise NotImplementedError