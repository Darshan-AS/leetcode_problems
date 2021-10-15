from itertools import chain

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def find_path(start: int, end: int):
            yield from (
                chain((start,), path)
                for i in graph[start]
                for path in find_path(i, end)
            ) if start != end else ((end,),)
            
        return list(map(list, find_path(0, len(graph) - 1)))
