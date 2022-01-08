from typing import List
from medLayer.interface.ilayer import ILayer


class IHost:
  layers: List[ILayer]