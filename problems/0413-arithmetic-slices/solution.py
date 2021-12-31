class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diffs = map(operator.sub, islice(nums, 1, None), nums)
        slices = (s for _, s in groupby(diffs))
        slices_len = map(lambda s: sum(1 for _ in s) + 1, slices) # +1 due to diff-slice having len - 1
        return sum((n * (n + 1) // 2) - n - (n - 1) for n in slices_len)

