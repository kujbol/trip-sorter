import enum
from dataclasses import dataclass

from trip_sorter.models.place import Place


class TripType(enum.Enum):
    plane = 'plane'
    train = 'train'
    bus = 'bus'
    taxi = 'taxi'
    foot = 'foot'


@dataclass
class Trip:
    id: int
    type: TripType
    source: Place
    target: Place


