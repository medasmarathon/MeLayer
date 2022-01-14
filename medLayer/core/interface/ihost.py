from typing import List
from .ilayer import ILayer
from .irelation import IRelation


class IHost:
  name: str
  layers: List[ILayer]
  interactions: List[IRelation]