class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned_duration = 0
        max_time = 0
        for t in timeSeries:
            poisoned_duration += duration - max(max_time - t, 0)
            max_time = t + duration
        return poisoned_duration
