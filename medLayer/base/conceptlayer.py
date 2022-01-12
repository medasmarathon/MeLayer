from medLayer.core.interface.ilayer import ILayer


class ConceptLayer(ILayer):

  def __init__(self, name: str, order: int):
    super().__init__()
    self.name = name
    self.order = order
    self.nodes = []