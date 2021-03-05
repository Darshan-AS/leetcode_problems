class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        max_square_length = prev_dp_j = 0
        dp = [0] * (n + 1)
        for i, j in product(range(m), range(n)):
            dp[j], prev_dp_j = (min(dp[j], dp[j - 1], prev_dp_j) + 1 if matrix[i][j] == "1" else 0, dp[j])
            max_square_length = max(max_square_length, dp[j])

        return max_square_length ** 2
