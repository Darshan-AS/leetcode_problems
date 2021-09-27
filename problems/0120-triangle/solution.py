class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Bottom up iterative DP
        
        totals = tuple(triangle[-1])
        while len(totals) != 1:
            row = len(totals) - 1
            totals = tuple(min(totals[i], totals[i + 1]) + triangle[row - 1][i] for i in range(row))
        
        return totals[0]
