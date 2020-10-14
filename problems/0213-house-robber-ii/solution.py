from functools import reduce

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def rob_next(res, v):
            a, b = res
            return (b, x) if (x := a + v) > b else (max(a, b), max(a, b))
        
        return max(reduce(rob_next, nums[:-1], (0, 0))[1], reduce(rob_next, nums[1:], (0, 0))[1])
