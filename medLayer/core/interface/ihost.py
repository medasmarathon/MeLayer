from typing import List
from .ilayer import ILayer
from .irelation import IRelation


class IHost:
  layers: List[ILayer]
  interactions: List[IRelation]