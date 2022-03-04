class Solution:
    def champagneTower(self, poured: int, r: int, c: int) -> float:
        dp = [0] * (r + 2)
        dp[1] = poured
        
        for i, j in product(range(1, r + 1), range(r + 1)):
            k = j + 1
            prev = dp[j] if j == 0 else prev
            prev, dp[k] = dp[k], (max(prev - 1, 0) + max(dp[k] - 1, 0)) / 2
        
        return min(dp[c + 1], 1.0)
