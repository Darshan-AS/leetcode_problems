class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diffs = map(operator.sub, islice(nums, 1, None), nums)
        slices = (s for _, s in groupby(diffs))
        slices_len = map(lambda s: sum(1 for _ in s) + 1, slices) # +1 due to diff-slice having len - 1
        return sum(n * (n + 1) // 2 for l in slices_len if (n := l - 2) > 0) # l - 2 to avoid counting 2 len slices

