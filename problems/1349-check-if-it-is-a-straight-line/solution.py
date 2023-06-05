class Solution:
    def checkStraightLine(self, points: list[list[int]]) -> bool:
        return all(starmap(eq, pairwise(starmap(lambda p, q: ((q[1] - p[1]) / (q[0] - p[0])) if (q[0] - p[0]) else inf, pairwise(points)))))
