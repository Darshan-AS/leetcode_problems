class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        dp = [math.inf] * (n + 1)
        dp[n - 1] = 1
        
        for i, j in product(range(m - 1, -1, -1), range(n - 1, -1, -1)):
            k = j
            dp[k] = max(min(dp[k + 1], dp[k]) - dungeon[i][j], 1)
        
        return dp[0]
            
