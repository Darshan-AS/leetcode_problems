class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        dp = defaultdict(lambda: 1)
        for r in range(len(nums)):
            for l in range(r):
                d = nums[r] - nums[l]
                dp[(r, d)] = dp[(l, d)] + 1
        return max(dp.values())
