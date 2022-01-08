from enum import Enum


class Event(Enum):
  COEXISTING = "Coexisting"
  FEED_FORWARD = "Feed Forward"
  FEED_BACK = "Feed Back"


class IInfluence:
  event: Event
  coefficient: float