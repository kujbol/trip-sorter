class TripSorter:
    """
    One time used object, It should be disposed after


    """
    def __init__(self, algorithm, input_handler, output_handler):
        self.algorithm = algorithm
        self.input_handler = input_handler
        self.output_handler = output_handler

    def sort_trips(self, trips):
        serialized_trips = self.input_handler.serialize(trips)

        for trip in serialized_trips:
            self.algorithm.add_trip(
                source_id=trip.source.id,
                target_id=trip.target.id,
                trip_id=trip.id,
            )

        sorted_trips = self.algorithm.sort_trips()

        return