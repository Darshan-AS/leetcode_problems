class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        @cache
        def ways(k: int) -> int:
            return sum(ways(k - x) for x in nums) if k > 0 else k == 0
        
        return ways(target)
