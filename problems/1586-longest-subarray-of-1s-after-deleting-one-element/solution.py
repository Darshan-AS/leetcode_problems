class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        streaks_of_1s = accumulate(nums, lambda a, x: (a + 1) * (x != 0), initial=0)
        streaks_at_0 = compress(streaks_of_1s, map(not_, chain(nums, (0,))))
        return max(starmap(add, pairwise(streaks_at_0)), default=len(nums) - 1)
