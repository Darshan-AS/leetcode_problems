class Solution:
    def canMakeArithmeticProgression(self, nums: list[int]) -> bool:        
        first, last, n = min(nums), max(nums), len(nums)
        diff, r = divmod(last - first, n - 1)
        return r == 0 and (diff == 0 or set(range(first, last + 1, diff)) == set(nums))
