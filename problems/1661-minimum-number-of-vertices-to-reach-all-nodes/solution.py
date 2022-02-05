class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> Iterable[int]:
        all_vertices = set(range(n))
        reachable_vertices = {v for _, v in edges}
        
        return all_vertices - reachable_vertices
