class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        time = sorted(map(truediv, dist, speed))
        killed = takewhile(truth, map(gt, time, count()))
        return sum(killed)
