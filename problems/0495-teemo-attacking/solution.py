class Solution:
    def findPoisonedDuration(self, time_series: list[int], duration: int) -> int:
        return sum(min(t2 - t1, duration) for t1, t2 in pairwise(time_series)) + duration
