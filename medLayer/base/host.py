from medLayer.core.interface import IHost


class Host(IHost):

  def __init__(self, name: str):
    super().__init__()
    self.name = name
    self.layers = []
