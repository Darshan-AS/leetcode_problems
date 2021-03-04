class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = 0
        for i in nums:
            seen ^= 1 << i
        seen <<= 1
        for i in range(len(nums) + 1):
            seen >>= 1
            if not seen % 2:
                return i
