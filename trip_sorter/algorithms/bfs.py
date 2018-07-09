from collections import defaultdict, deque

from trip_sorter.algorithms import InvalidData


class BFSAlgorithm:
    """
    This algorithm can be used only for simplest case. It can be applied
    for case where all trips needs to be used and there are no round trips.
    """

    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.out_degree = defaultdict(lambda: 0)
        self.in_degree = defaultdict(lambda: 0)

    def add_trip(self, source, target, trip_id):
        self.adjacency_list[source].append(
            {'target': target, 'trip_id': trip_id}
        )

        self.in_degree[target] = self.in_degree[target] + 1
        self.out_degree[source] = self.out_degree[source] + 1

    def sort_trips(self):
        source, target = self._find_source(), self._find_targets()
        queue = deque()
        visited = dict()

        queue.append(source)
        while len(queue) > 0:
            actual_place = queue.pop()
            if actual_place == target:
                return self._calculate_path(source, target, visited)

            for neighbour in self.adjacency_list[actual_place]:
                if not visited.get(neighbour['target']):
                    visited[neighbour['target']] = {
                        'visited_from': actual_place,
                        'trip_id': neighbour['trip_id']
                    }

                    queue.append(neighbour['target'])

        raise InvalidData('Path not found from source to target')

    def _find_targets(self):
        potential_starts = []
        for place, in_degree in self.in_degree.items():
            if in_degree == 1 and place not in self.out_degree:
                potential_starts.append(place)

        if len(potential_starts) != 1:
            raise InvalidData(
                f'Expected 1 potential target, found: {len(potential_starts)}'
            )

        return potential_starts[0]

    def _find_source(self):
        potential_starts = []
        for place, out_degree in self.out_degree.items():
            if out_degree == 1 and place not in self.in_degree:
                potential_starts.append(place)

        if len(potential_starts) != 1:
            raise InvalidData(
                f'Expected 1 potential source, found: {len(potential_starts)}'
            )

        return potential_starts[0]

    def _calculate_path(self, source, target, visited):
        actual = target
        trips = []
        while actual != source:
            visited_by = visited[actual]
            trips.append(visited_by['trip_id'])
            actual = visited_by['visited_from']

        return list(reversed(trips))
