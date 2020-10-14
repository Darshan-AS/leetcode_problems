from functools import reduce

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_next(res, v):
            a, b = res
            return (b, x) if (x := a + v) > b else (max(a, b), max(a, b))
        
        return reduce(rob_next, nums, (0, 0))[1]
