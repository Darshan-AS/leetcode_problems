class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp = [0] * (n + 2)
        dp[0] = dp[-1] = prev = math.inf
        for i, j in product(range(m), range(n)):
            k = j + 1
            prev = prev if j > 0 else math.inf
            prev, dp[k] = dp[k], min(prev, dp[k], dp[k + 1]) + matrix[i][j]
        
        return min(dp)
