import copy

import pytest

from trip_sorter.models.place import Place
from trip_sorter.models.trip import Trip, TripDetails, TripType


@pytest.fixture()
def source_place():
    return Place(
        id=1,
        place_name='Source',
    )


@pytest.fixture()
def target_place():
    return Place(
        id=1,
        place_name='Target',
    )


@pytest.fixture()
def trip_details_plane():
    return TripDetails(
        type=TripType.plane,
        transport_id='PL-1234',
        transport_start_place='gate 13',
        seat='A13',
    )


@pytest.fixture()
def trip_details_train():
    return TripDetails(
        type=TripType.train,
        transport_id='PKP-11',
        transport_start_place='Track 3',
        seat=None,
    )


@pytest.fixture()
def trip(trip_details_plane, source_place, target_place):
    return Trip(
        id=0,
        trip_details=trip_details_plane,
        source=source_place,
        target=target_place,
    )


@pytest.fixture()
def trip_2(trip_details_train, source_place, target_place):
    return Trip(
        id=1,
        trip_details=trip_details_train,
        source=source_place,
        target=target_place,
    )
