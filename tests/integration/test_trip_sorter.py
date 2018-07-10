import pytest

from trip_sorter import TripSorter
from trip_sorter.serializers.input import InputSerializer
from trip_sorter.serializers.output import OutputSerializer
from trip_sorter.algorithms.bfs import BFSAlgorithm
from trip_sorter.errors import InvalidData
from trip_sorter.models.trip import TripType


@pytest.fixture()
def trip_sorter():
    algorithm = BFSAlgorithm()
    input_serializer, output_serializer = InputSerializer(), OutputSerializer()
    return TripSorter(
        algorithm=algorithm,
        input_serializer=input_serializer,
        output_serializer=output_serializer,
    )


def test_working_inputs_tests(input_working_trip, trip_sorter):
    result = trip_sorter.sort_trips(input_working_trip)

    assert len(result) == len(input_working_trip) + 1


def test_not_working_inputs(input_not_working_trip, trip_sorter):
    with pytest.raises(InvalidData):
        trip_sorter.sort_trips(input_not_working_trip)


def test_full_integration(input_simple_2_trip_path, trip_sorter):
    modified_input = list(input_simple_2_trip_path)
    modified_input[0]['trip_details']['type'] = TripType.train.value
    modified_input[1]['trip_details']['type'] = TripType.plane.value

    result = trip_sorter.sort_trips(input_simple_2_trip_path)

    assert result == [
        'Take train No13234 from Place 1 to Place 2. Gate 13, Seat A13',
        'From place 2 to place 3 Airport, take flight No13234. Gate 13, Seat A13',  # noqa
        'You have arrived at your final destination.'
    ]
