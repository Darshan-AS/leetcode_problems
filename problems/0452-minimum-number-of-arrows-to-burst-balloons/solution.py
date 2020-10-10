class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        end = float('-inf')
        shots = 0     
        points.sort(key=lambda x: x[1])
        for point in points:
            if point[0] > end:
                shots += 1
                end = point[1]
        return shots
