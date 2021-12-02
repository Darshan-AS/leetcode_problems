class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = 0, 0
        for c in cost:
            a, b = b, min(a, b) + c
        return min(a, b)
