class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        T = TypeVar('T')
        Graph = Mapping[T, Container[T]]

        def is_dag(g: Graph, root: T) -> bool:
            seen: Container[T] = set()

            @cache
            def helper(node: T) -> bool:
                return node not in seen and (seen.add(node), all(map(helper, g[node])), seen.remove(node))[1]
            
            return helper(root)
        
        graph = defaultdict(set, {-1: set(range(numCourses))})
        for a, b in prerequisites: graph[a].add(b)

        return is_dag(graph, -1)
