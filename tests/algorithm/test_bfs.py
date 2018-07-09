import pytest

from trip_sorter.algorithms import InvalidData
from trip_sorter.algorithms.bfs import BFSAlgorithm


@pytest.fixture()
def algorithm():
    return BFSAlgorithm()


def test_simple_case(algorithm):
    algorithm.add_trip(1, 2, 0)
    algorithm.add_trip(2, 3, 1)

    trips = algorithm.sort_trips()

    assert trips == [0, 1, ]


def test_2_places_case(algorithm):
    """
    1 --> 2
       0
    """
    algorithm.add_trip(1, 2, 0)

    trips = algorithm.sort_trips()

    assert trips == [0, ]


def test_10_reversed_places(algorithm):
    """
    10 --> 9 --> 8 --> ... --> 1
        9     8     7       1

    result == [9, 8, 7, .. , 1]
    """
    for i in range(10, 1, -1):
        algorithm.add_trip(i, i-1, i-1)

    result = algorithm.sort_trips()
    assert result == list(range(9, 0, -1))


def test_no_potential_start_loop(algorithm):
    """
    1 --> 2
    ^  0  |
    ------
       1
    """

    algorithm.add_trip(1, 2, 0)
    algorithm.add_trip(2, 1, 1)

    with pytest.raises(InvalidData) as exc:
        algorithm.sort_trips()


def test_2_potential_sources(algorithm):
    """
    1 --> 2
       0  ^
          |
    3 ----
        1
    """

    algorithm.add_trip(1, 2, 0)
    algorithm.add_trip(3, 2, 1)

    with pytest.raises(InvalidData) as exc:
        algorithm.sort_trips()


def test_2_potential_targets(algorithm):
    """
    1 --> 2
    |  0
     ---> 3
      1
    """
    algorithm.add_trip(1, 2, 0)
    algorithm.add_trip(1, 3, 1)

    with pytest.raises(InvalidData) as exc:
        algorithm.sort_trips()
