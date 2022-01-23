class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(accumulate(nums, lambda a, x: a + 1 if x == 1 else 0, initial=0))
