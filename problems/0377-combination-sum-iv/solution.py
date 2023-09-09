class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        return (ways := cache(lambda k: sum(ways(k - x) for x in nums) if k > 0 else k == 0))(target)
