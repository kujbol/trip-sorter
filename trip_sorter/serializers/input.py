from trip_sorter.errors import InvalidInput
from trip_sorter.models.place import Place, PlaceType
from trip_sorter.models.trip import Trip, TripType, TripDetails


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
        source: dict
            id: id of the source for the trip
            name: name of the place
            type: type of the source, it can be one from PlaceType
        target: dict
            id: id of the source for the trip
            name: name of the place
            type: type of the source, it can be one from PlaceType
        trip_details: dict
            type: str, type of trip, it can be one from TripType
            transport_id: str, transport real identification name
            transport_start_place: str, transport start place for example train station / gate 783
            seat: str, stea number of transport
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
                id=trip_id,
                source=source,
                target=target,
                trip_details=self.serialize_trip_details(
                    trip_id, trip['trip_details']
                )
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

    def serialize_trip_details(self, trip_id, trip_details) -> TripDetails:
        try:
            return TripDetails(
                type=trip_details['type'],
                transport_id=trip_details.get('transport_id'),
                transport_start_place=trip_details.get('transport_start_place'),
                seat=trip_details.get('seat'),
            )
        except KeyError as exc:
            raise InvalidInput(
                f'Invalid trip details for trip: {trip_id}, missing key: {exc}'
            )
