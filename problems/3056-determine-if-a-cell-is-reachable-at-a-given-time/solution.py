class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        d = max(abs(sx - fx), abs(sy - fy))
        return (d != 0 or t != 1) and t >= d
