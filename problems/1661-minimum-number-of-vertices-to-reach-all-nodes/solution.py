class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        return set(range(n)) - set(v for _, v in edges)
