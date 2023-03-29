class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        return sum(takewhile(lambda x: x >= 0, accumulate(sorted(satisfaction, reverse=True))))
