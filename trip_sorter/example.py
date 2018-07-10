from trip_sorter import TripSorter
from trip_sorter.algorithms.bfs import BFSAlgorithm
from trip_sorter.serializers.input import InputSerializer
from trip_sorter.serializers.output import OutputSerializer

example_from_file = [
    {
        'trip_details': {
            'type': 'plane',
            'transport_id': 'SK455',
            'transport_start_place': 'gate 45B',
            'seat': '3A'
        },
        'source': {'id': 3, 'name': 'Gerona Airport'},
        'target': {'id': 4, 'name': 'Stockholm Airport'}
    },
    {
        'trip_details': {
            'type': 'plane',
            'transport_id': 'SK22',
            'transport_start_place': 'gate 22',
            'seat': '7B'
        },
        'source': {'id': 4, 'name': 'Stockholm Airport'},
        'target': {'id': 5, 'name': 'New York JFK'}
    },
    {
        'trip_details': {
            'type': 'bus',
            'transport_id': '"airport"',
        },
        'source': {'id': 2, 'name': 'Barcelona'},
        'target': {'id': 3, 'name': 'Gerona Airport'}
    },
    {
        'trip_details': {
            'type': 'train',
            'transport_id': '78A',
            'seat': '45B'
        },
        'source': {'id': 1, 'name': 'Madrid'},
        'target': {'id': 2, 'name': 'Barcelona'}
    },
]

algorithm = BFSAlgorithm()
input_serializer, output_serializer = InputSerializer(), OutputSerializer()
trip_sorter = TripSorter(
    algorithm=algorithm,
    input_serializer=input_serializer,
    output_serializer=output_serializer,
)

result = trip_sorter.sort_trips(example_from_file)

print('\n'.join(result))
