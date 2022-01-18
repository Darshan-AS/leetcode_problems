class Solution:
    def canMakeArithmeticProgression(self, nums: List[int]) -> bool:        
        first, last, n = min(nums), max(nums), len(nums)
        diff, r = divmod(last - first, n - 1)
        return diff == 0 or (r == 0 and set(range(first, last + 1, diff)) == set(nums))
