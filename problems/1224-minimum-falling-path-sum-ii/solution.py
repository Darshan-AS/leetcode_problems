class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def two_mins(seq):
            return reduce(
                lambda a, x: (x, a[0]) if x < a[0] else ((a[0], x) if x < a[1] else a),
                seq,(math.inf, math.inf)
            ) if len(seq) >= 2 else (seq[0], seq[0])
        
        m, n = len(grid), len(grid[0])
        
        dp = [0] * n
        
        for i in range(m):
            min_1, min_2 = two_mins(dp)
            for j in range(n):
                dp[j] = (min_1 if dp[j] != min_1 else min_2) + grid[i][j]
        
        return min(dp)
