from functools import reduce

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_next(res, x):
            a, b = res
            if (next_x := a + x) > b: return (b, next_x)
            else: return max(a, b), max(a, b)
        
        return reduce(rob_next, nums, (0, 0))[1]
