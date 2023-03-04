class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        indexes = lambda f: accumulate(range(len(nums)), lambda a, x: x if f(nums[x]) else a, initial=-1)

        left_bounds = indexes(lambda num: num < minK or num > maxK)
        maxs = indexes(lambda num: num == maxK)
        mins = indexes(lambda num: num == minK)

        count_fn = lambda lb, mx, mn: max(0, min(mx, mn) - lb)
        return sum(map(count_fn, left_bounds, maxs, mins))
