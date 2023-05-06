class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        s_nums = sorted(nums)
        return sum(
            pow(2, bisect.bisect(s_nums, y, i) - 1 - i, 1_000_000_007)
            for i, x in enumerate(s_nums)
            if (y := target - x) >= x
        ) % 1_000_000_007
