class PlaceSerializer:
    @staticmethod
    def serialize(trip):
        return f'from {trip.source.place_name} to {trip.target.place_name}'


class TransportIdSerializer:
    @staticmethod
    def serialize(trip):
        transport_id = trip.trip_details.transport_id
        if not transport_id:
            return 'with no number'
        return transport_id


class SeatSerializer:
    @staticmethod
    def serialize(trip):
        seat_number = trip.trip_details.seat
        if not seat_number:
            return 'No seat assignment'
        return f'Seat {seat_number}'


class TransportStartSerializer:
    @staticmethod
    def serialize(trip):
        transport_start = trip.trip_details.transport_start_place
        if not transport_start:
            return ''
        return f'{transport_start.capitalize()}'


class TrainSerializer:
    @staticmethod
    def serialize(trip):
        return (
            f'Take train {TransportIdSerializer.serialize(trip)} '
            f'{PlaceSerializer.serialize(trip)}. '
            f'{TransportStartSerializer.serialize(trip)}, '
            f'{SeatSerializer.serialize(trip)}'
        )


class PlaneSerializer:
    @staticmethod
    def serialize(trip):
        return (
            f'{PlaceSerializer.serialize(trip).capitalize()} Airport, '
            f'take flight {TransportIdSerializer.serialize(trip)}. '
            f'{TransportStartSerializer.serialize(trip)}, '
            f'{SeatSerializer.serialize(trip)}'
        )


class BusSerializer:
    @staticmethod
    def serialize(trip):
        return (
            f'Take the {TransportIdSerializer.serialize(trip)} bus '
            f'{PlaceSerializer.serialize(trip).capitalize()}. '
            f'{TransportStartSerializer.serialize(trip)}, '
            f'{SeatSerializer.serialize(trip)}'
        )
