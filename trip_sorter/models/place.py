import enum
from dataclasses import dataclass


class PlaceType(enum.Enum):
    city = 'city'
    country = 'country'
    street = 'street'
    building = 'building'


@dataclass
class Place:
    type: PlaceType
    id: int
    place_name: str
