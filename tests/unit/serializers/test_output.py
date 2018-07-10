import pytest

from trip_sorter.models.trip import TripType
from trip_sorter.serializers.output import OutputSerializer


@pytest.mark.parametrize('param_trip_type, expected_keyword', [
    (TripType.bus, 'bus'),
    (TripType.plane, 'Airport'),
    (TripType.train, 'train'),
])
def test_output_serialize_1_trip(trip, param_trip_type, expected_keyword):
    trip.trip_details.type = param_trip_type
    sorted_trips = [0, ]
    serialized_trips = {0: trip}

    result = OutputSerializer().serialize(serialized_trips, sorted_trips)

    assert len(result) == 2
    assert expected_keyword in result[0]
    assert result[1] == OutputSerializer().finalize_journey()


def test_many_output(trip, trip_2):
    sorted_trips = [0, 1]
    serialized_trips = {0: trip, 1: trip_2}

    result = OutputSerializer().serialize(serialized_trips, sorted_trips)
    assert len(result) == 3

    # check order
    assert 'Airport' in result[0]
    assert 'train' in result[1]
