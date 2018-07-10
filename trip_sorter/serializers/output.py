from trip_sorter.models.trip import TripType
from trip_sorter.serializers.trip import (
    BusSerializer,
    PlaneSerializer,
    TrainSerializer,
)


class OutputSerializer:
    mapping = {
        TripType.bus: BusSerializer,
        TripType.plane: PlaneSerializer,
        TripType.train: TrainSerializer,
    }

    def serialize(self, serialized_trips, sorted_trip_ids: list):
        """
        :param serialized_trips: serialized input trips in form of dictionary of
        Trip where key is trip.id
        :param sorted_trips: list of trip ids sorted by algorithm
        """

        journey_tips = []

        for trip_id in sorted_trip_ids:
            trip = serialized_trips[trip_id]
            out_trip_serializer = self.mapping[trip.trip_details.type]
            journey_tips.append(out_trip_serializer.serialize(trip))

        journey_tips.append(self.finalize_journey())

        return journey_tips

    def finalize_journey(self):
        return 'You have arrived at your final destination.'
