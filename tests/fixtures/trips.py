import pytest


@pytest.fixture()
def simple_2_trip_path():
    """
    1 --> 2 --> 3
       0     1
    """
    return [
        (1, 2, 0),
        (2, 3, 1),
    ]


@pytest.fixture()
def simple_1_trip_path():
    """
    1 --> 2
       0
    """
    return [
        (1, 2, 0),
    ]


@pytest.fixture()
def simple_10_reversed_places():
    """
    10 --> 9 --> 8 --> ... --> 1
        9     8     7       1

    result == [9, 8, 7, .. , 1]
    """
    return [
        (i, i - 1, i - 1)
        for i in range(10, 1, -1)
    ]


@pytest.fixture()
def no_potential_start_loop():
    """
    1 --> 2
    ^  0  |
    ------
       1
    """
    return [
        (1, 2, 0),
        (2, 1, 1),
    ]


@pytest.fixture()
def multiple_potential_sources():
    """
    1 --> 2
       0  ^
          |
    3 ----
        1
    """
    return [
        (1, 2, 0),
        (3, 2, 1)
    ]


@pytest.fixture()
def multiple_2_potential_targets():
    """
    1 --> 2
    |  0
     ---> 3
      1
    """
    return [
        (1, 2, 0),
        (1, 3, 1),
    ]


@pytest.fixture()
def not_all_ticket_connected():
    """
    1 --> 2  3 --> 4
       0        1
    """

    return [
        (1, 2, 0),
        (3, 4, 1)
    ]


@pytest.fixture()
def no_trips():
    return []


@pytest.fixture(params=[
    simple_2_trip_path,
    simple_1_trip_path,
    simple_10_reversed_places,
    no_trips,
])
def working_trip(request):
    return request.param()


@pytest.fixture(params=[
    no_potential_start_loop,
    multiple_potential_sources,
    multiple_2_potential_targets,
    not_all_ticket_connected
])
def not_working_trip(request):
    return request.param()
