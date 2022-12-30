from collections.abc import *

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        T = TypeVar('T')
        Graph = Mapping[T, Collection[T]]
        Path = Iterable[T]

        def dag_paths(dag: Graph, source: T, destination: T) -> Iterator[Path]:
            all_nbr_paths = chain.from_iterable(
                dag_paths(dag, nbr, destination)
                for nbr in dag[source]
            ) if source != destination else (deque(),)

            return map(lambda p: p.appendleft(source) or p, all_nbr_paths)
        
        return list(dag_paths(graph, 0, len(graph) - 1))
