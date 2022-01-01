class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i, j in product(range(n), range(amount + 1)):
            dp[j] = dp[j] + (dp[j - coins[i]] if j >= coins[i] else 0)
        
        return dp[-1]
