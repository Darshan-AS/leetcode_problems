class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        max_square_side = 0
        dp = [0] * (n + 1)
        prev = 0
        
        for i, j in product(range(m), range(n)):
            k = j + 1
            prev = prev if j > 0 else 0
            prev, dp[k] = dp[k], min(dp[k - 1], dp[k], prev) + 1 if matrix[i][j] == '1' else 0
            max_square_side = max(max_square_side, dp[k])
        
        return max_square_side ** 2
