from random import choice

import pytest

from trip_sorter.example import example_from_file
from trip_sorter.models.trip import TripType


def create_input_from_case(case):
    def create_trip_detail(trip_type: TripType):
        return {
            'type': trip_type.value,
            'transport_id': 'No13234',
            'transport_start_place': 'gate 13',
            'seat': 'A13'
        }

    return [
        {
            'trip_details': create_trip_detail(choice(list(TripType))),
            'source': {
                'id': source_id,
                'name': f'Place {source_id}',
            },
            'target': {
                'id': target_id,
                'name': f'Place {target_id}',
            },
        }
        for source_id, target_id, _ in case
    ]


@pytest.fixture()
def input_simple_2_trip_path(simple_2_trip_path):
    return create_input_from_case(simple_2_trip_path)


@pytest.fixture()
def input_simple_1_trip_path(simple_1_trip_path):
    return create_input_from_case(simple_1_trip_path)


@pytest.fixture()
def input_simple_10_reversed_places(simple_10_reversed_places):
    return create_input_from_case(simple_10_reversed_places)


@pytest.fixture()
def input_no_potential_start_loop(no_potential_start_loop):
    return create_input_from_case(no_potential_start_loop)


@pytest.fixture()
def input_multiple_potential_sources(multiple_potential_sources):
    return create_input_from_case(multiple_potential_sources)


@pytest.fixture()
def input_multiple_2_potential_targets(multiple_2_potential_targets):
    return create_input_from_case(multiple_2_potential_targets)


@pytest.fixture()
def input_working_trip(working_trip):
    return create_input_from_case(working_trip)


@pytest.fixture()
def input_not_working_trip(not_working_trip):
    return create_input_from_case(not_working_trip)


@pytest.fixture()
def example():
    return example_from_file
