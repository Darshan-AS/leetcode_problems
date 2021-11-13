class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return reduce(lambda s, n: 1 if n >= s else s + 1, reversed(nums), 0) == 1
