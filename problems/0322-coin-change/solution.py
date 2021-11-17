class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        
        for i, j in product(range(n), range(amount + 1)):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1 if j >= coins[i] else math.inf)
        
        return -1 if dp[-1] == math.inf else dp[-1]
