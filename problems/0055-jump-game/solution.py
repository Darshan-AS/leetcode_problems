class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = 0
        for num in reversed(nums):
            if num >= steps: steps = 0
            steps += 1
        return steps == 1
