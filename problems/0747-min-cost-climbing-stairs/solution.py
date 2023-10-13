class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        return min(reduce(lambda a, x: (a[1], min(a) + x), cost, (0, 0)))
        
