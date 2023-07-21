class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        return max(accumulate(starmap(lt, pairwise(nums)), lambda a, x: a * x + x, initial=0)) + 1
