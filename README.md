# Trip Sorter
> Python library for sorting trips, and creating best route and trip description 

# Usage
You need to initialize TripSorter, you can chose algorithm, or write your own
and expand functionality. More details can be found in doc strings.

example usage
```python
from trip_sorter import TripSorter
from trip_sorter.algorithms.bfs import BFSAlgorithm
from trip_sorter.serializers.input import InputSerializer
from trip_sorter.serializers.output import OutputSerializer

trip_sorter = TripSorter(
    algorithm=BFSAlgorithm(),
    input_serializer=InputSerializer(),
    output_serializer=OutputSerializer(),
)

result = trip_sorter.sort_trips(trips)
```

form working example check `trip_sorter.example`


#Running
* You can use docker compose, and start example or start tests 
```bash
docker-compose up example
docker-compose up tests
```

# Development
* You can run tests using docker-compose
* You can setup your local environment, simply install requiremets.txt and 
start coding
