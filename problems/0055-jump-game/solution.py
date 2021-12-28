class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return reduce(lambda a, x: max(a - 1, x) if a > 0 else -1, nums, 1) >= 0
