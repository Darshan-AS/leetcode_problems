def num_squares_dp(n):
    perfect_squares = map(lambda x: x * x, count(1))
    pool = list(takewhile(lambda x: x <= n, perfect_squares))

    dp = [math.inf] * (n + 1)
    dp[0] = 0

    for i, j in product(range(len(pool)), range(n + 1)):
        dp[j] = min(dp[j], dp[j - pool[i]] + 1 if j >= pool[i] else math.inf)

    return dp

class Solution:
    # Due to TLE, precompute and cache
    dp = num_squares_dp(10_000)
    
    def numSquares(self, n: int) -> int:
        return self.dp[n]


