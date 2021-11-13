from functools import reduce

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_(nums_):
            a, b = 0, 0
            for num in nums_:
                a, b = b, max(b, a + num)
            return b
        
        return max(rob_(nums[:-1]), rob_(nums[1:])) if len(nums) > 1 else nums[0]
