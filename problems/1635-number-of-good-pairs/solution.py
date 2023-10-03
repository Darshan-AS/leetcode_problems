class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return sum((n - 1) * n // 2 for n in Counter(nums).values())
