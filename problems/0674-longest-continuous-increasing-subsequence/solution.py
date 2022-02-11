class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        is_increasing = (a < b for a, b in pairwise(nums))
        cis = accumulate(is_increasing, lambda a, x: a + 1 if x else 0)
        return max(cis, default=0) + 1
