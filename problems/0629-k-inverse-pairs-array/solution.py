class Solution:
    
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0] * (k + 1)
        MAX = 1000000007

        for i in range(1, n + 1):
            next_dp = [0] * (k + 1)
            next_dp[0] = 1
            for j in range(1, k + 1):
                next_val = dp[j]
                prev_val = dp[j - i] if j - i >= 0 else 0
                next_dp[j] = (next_dp[j - 1] + next_val - prev_val + MAX) % MAX
            dp = next_dp

        return (dp[k] - (dp[k - 1] if k - 1 >= 0 else 0) + MAX) % MAX
