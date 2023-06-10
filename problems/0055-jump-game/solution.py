class Solution:
    def canJump(self, nums: list[int]) -> bool:
        r = 1
        for n in nums:
            if r <= 0: return False
            r = max(r - 1, n)
        return True

