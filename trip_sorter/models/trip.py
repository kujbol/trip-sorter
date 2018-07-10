import enum
from dataclasses import dataclass

from trip_sorter.models.place import Place


class TripType(enum.Enum):
    plane = 'plane'
    train = 'train'
    bus = 'bus'


@dataclass
class TripDetails:
    type: TripType
    transport_id: str
    transport_start_place: str
    seat: str


@dataclass
class Trip:
    id: int
    source: Place
    target: Place
    trip_details: TripDetails
