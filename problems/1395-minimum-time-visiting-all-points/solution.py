class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        return sum(max(abs(x1 - x2), abs(y1 - y2)) for (x1, y1), (x2, y2) in pairwise(points))
        
