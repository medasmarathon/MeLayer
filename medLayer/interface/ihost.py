from typing import List
from ilayer import ILayer
from iinteraction import IInteraction


class IHost:
  layers: List[ILayer]
  interactions: List[IInteraction]