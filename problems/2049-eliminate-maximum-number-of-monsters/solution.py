class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        return sum(takewhile(truth, map(gt, sorted(map(truediv, dist, speed)), count())))
