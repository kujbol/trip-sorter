import pytest

from trip_sorter.serializers.trip import (
    PlaceSerializer,
    SeatSerializer,
    TransportIdSerializer,
    TransportStartSerializer,

    BusSerializer,
    PlaneSerializer,
    TrainSerializer,
)


def test_place_serialize(trip):
    result = PlaceSerializer.serialize(trip)
    assert result == 'from Source to Target'


def test_transport_id_serialize(trip):
    result = TransportIdSerializer.serialize(trip)
    assert result == 'PL-1234'


def test_transport_id_serialize_no_id(trip):
    trip.trip_details.transport_id = None
    result = TransportIdSerializer.serialize(trip)
    assert result == 'with no number'


def test_seat_serialize(trip):
    result = SeatSerializer.serialize(trip)
    assert result == 'Seat A13'


def test_seat_serialize_no_seat(trip):
    trip.trip_details.seat = None
    result = SeatSerializer.serialize(trip)
    assert result == 'No seat assignment'


def test_transport_serialize(trip):
    result = TransportStartSerializer.serialize(trip)
    assert result == 'Gate 13, '


def test_transport_serialize_no_transport(trip):
    trip.trip_details.transport_start_place = None
    result = TransportStartSerializer.serialize(trip)
    assert result == ''


@pytest.mark.parametrize('serializer', [
    BusSerializer,
    PlaneSerializer,
    TrainSerializer,
])
def test_serialize_trip(trip, serializer):
    result = serializer.serialize(trip)
    assert result
