import pytest

from trip_sorter.errors import InvalidData
from trip_sorter.algorithms.bfs import BFSAlgorithm


@pytest.fixture()
def algorithm():
    return BFSAlgorithm()


def load_data(algorithm, case):
    for trip in case:
        algorithm.add_trip(*trip)


def test_simple_case(algorithm, simple_2_trip_path):
    load_data(algorithm, simple_2_trip_path)
    trips = algorithm.sort_trips()

    assert trips == [0, 1, ]


def test_2_places_case(algorithm, simple_1_trip_path):
    load_data(algorithm, simple_1_trip_path)
    trips = algorithm.sort_trips()

    assert trips == [0, ]


def test_10_reversed_places(algorithm, simple_10_reversed_places):
    load_data(algorithm, simple_10_reversed_places)

    result = algorithm.sort_trips()
    assert result == list(range(9, 0, -1))


def test_no_potential_start_loop(algorithm, no_potential_start_loop):
    load_data(algorithm, no_potential_start_loop)

    with pytest.raises(InvalidData) as exc:
        algorithm.sort_trips()

    assert 'Expected 1 potential source, found: 0' in exc.value.args[0]


def test_2_potential_sources(algorithm, multiple_potential_sources):
    load_data(algorithm, multiple_potential_sources)

    with pytest.raises(InvalidData) as exc:
        algorithm.sort_trips()

    assert 'Expected 1 potential source, found: 2' in exc.value.args[0]


def test_2_potential_targets(algorithm, multiple_2_potential_targets):
    load_data(algorithm, multiple_2_potential_targets)

    with pytest.raises(InvalidData) as exc:
        algorithm.sort_trips()

    assert 'Expected 1 potential source, found: 0' in exc.value.args[0]
