class TripSorter:
    """One time used object, It should be disposed after sorting trips
    """
    def __init__(self, algorithm, input_serializer, output_serializer):
        """
        :param algorithm: algorithm used for sorting, it needs to provide
        add_trip method and sort trips which will return ids of sorted trips
        :param input_serializer: handles input, input format can be found in
        input serializers description, it needs to provide
        serialized_trips and places as dictionary where key is place_id/trip_id
        :param output_serializer: handles output format
        """
        self.algorithm = algorithm
        self.input_serializer = input_serializer
        self.output_serializer = output_serializer

    def sort_trips(self, trips):
        """Gets unordered list of trips and calculate correct order.
        Uses for it algorithm provided in init and input/output serializer.
        """
        serialized_trips = self.input_serializer.serialize(trips)

        for trip in serialized_trips.values():
            self.algorithm.add_trip(
                source_id=trip.source.id,
                target_id=trip.target.id,
                trip_id=trip.id,
            )

        sorted_trip_ids = self.algorithm.sort_trips()

        return self.output_serializer.serialize(
            serialized_trips=self.input_serializer.serialized_trips,
            sorted_trip_ids=sorted_trip_ids,
        )
