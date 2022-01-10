from ..dataclass import Node


def say_yes(self: Node):
  return 'Yes'


Node.say_yes = say_yes
