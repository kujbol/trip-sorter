import pytest

from trip_sorter.errors import InvalidInput
from trip_sorter.serializers.input import InputSerializer


@pytest.fixture()
def serializer():
    return InputSerializer()


def test_input_handler_simple_2_trip_path(
        input_simple_2_trip_path, serializer
):
    result = serializer.serialize(input_simple_2_trip_path)
    assert len(input_simple_2_trip_path) == len(result)

    trip_0 = result[0]
    trip_1 = result[1]

    assert trip_0.id == 0
    assert trip_1.id == 1

    assert trip_0.target == trip_1.source

    for place in [trip_0.source, trip_0.target, trip_1.target]:
        assert serializer.serialized_places[place.id] == place

    assert trip_0.id in serializer.serialized_trips
    assert trip_1.id in serializer.serialized_trips


def test_inputs(input_working_trip, serializer):
    result = serializer.serialize(input_working_trip)

    assert len(result) == len(input_working_trip)


@pytest.mark.parametrize('param_missing_key', [
    'type', 'source', 'target'
])
def test_invalid_trip(input_simple_2_trip_path, param_missing_key, serializer):
    del input_simple_2_trip_path[0][param_missing_key]

    with pytest.raises(InvalidInput) as exc:
        serializer.serialize(input_simple_2_trip_path)

    assert 'Invalid trip 0' in exc.value.args[0]


@pytest.mark.parametrize('param_missing_key', [
    'name', 'id'
])
def test_invalid_trip(input_simple_2_trip_path, param_missing_key, serializer):
    del input_simple_2_trip_path[0]['source'][param_missing_key]

    with pytest.raises(InvalidInput) as exc:
        serializer.serialize(input_simple_2_trip_path)

    assert 'Invalid place for trip: 0' in exc.value.args[0]


def test_invalid_trip_details(input_simple_2_trip_path, serializer):
    del input_simple_2_trip_path[0]['trip_details']['type']

    with pytest.raises(InvalidInput) as exc:
        serializer.serialize(input_simple_2_trip_path)

    assert (
        "Invalid trip details for trip: 0, missing key: 'type'"
        in exc.value.args[0]
    )


def test_invalid_invalid_type(input_simple_2_trip_path, serializer):
    input_simple_2_trip_path[0]['trip_details']['type'] = 'INVALID'

    with pytest.raises(InvalidInput):
        serializer.serialize(input_simple_2_trip_path)
