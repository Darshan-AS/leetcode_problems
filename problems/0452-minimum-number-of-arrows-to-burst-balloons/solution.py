class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        
        start = float('-inf')
        end = float('inf')
        shots = 1
        
        points.sort()
        for a, b in points:
            if a > end:
                shots += 1
                start, end = a, b
            else:
                start = max(start, a)
                end = min(end, b)
        return shots
