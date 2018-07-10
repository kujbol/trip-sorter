import pytest

from trip_sorter import TripSorter
from trip_sorter.serializers.input import InputSerializer
from trip_sorter.serializers.output import OutputSerializer
from trip_sorter.algorithms.bfs import BFSAlgorithm
from trip_sorter.errors import InvalidData


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
