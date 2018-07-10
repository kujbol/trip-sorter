from trip_sorter.errors import InvalidInput
from trip_sorter.models.place import Place, PlaceType
from trip_sorter.models.trip import Trip, TripType


class InputSerializer:
    """
    Validates input format and serialize it to readable format by the rest of
    the application

    One time usable object, should be disposed after usage
    """
    def __init__(self):
        self.serialized_places = {}
        self.serialized_trips = []

    def serialize(self, trips: list):
        """
        Expected format - list of objects with properties:
        type: str, type of trip, it can be one from TripType
        source: obj
            id: id of the source for the trip
            name: name of the place
            type: type of the source, it can be one from PlaceType
        target: obj
            id: id of the source for the trip
            name: name of the place
            type: type of the source, it can be one from PlaceType
        """
        for trip_id, trip in enumerate(trips):
            trip = self.serialize_trip(trip_id, trip)
            self.serialized_trips.append(trip)

        return self.serialized_trips

    def serialize_trip(self, trip_id: int, trip: dict):
        try:
            source = self.serialize_place(trip_id, trip['source'])
            target = self.serialize_place(trip_id, trip['target'])

            trip = Trip(
                type=TripType[trip['type']],
                id=trip_id,
                source=source,
                target=target,
            )

            return trip

        except KeyError as exc:
            raise InvalidInput(
                f'Invalid trip {trip_id}, missing key: {exc}'
            )

    def serialize_place(self, trip_id: int, place: dict) -> Place:
        try:
            place_id = place['id']

            if place_id in self.serialized_places:
                return self.serialized_places[place_id]

            place = Place(
                id=place_id,
                type=PlaceType[place['type']],
                place_name=place['name']
            )
            self.serialized_places[place_id] = place
            return place

        except KeyError as exc:
            raise InvalidInput(
                f'Invalid place for trip: {trip_id}, missing key: {exc}'
            )
