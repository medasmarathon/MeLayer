from medLayer.interface.inode import INode
from ..base import Node


def say_yes(self: INode):
  return 'Yes'


Node.say_yes = say_yes