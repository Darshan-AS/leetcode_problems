class Solution:
    def bestTeamScore(self, scores_: list[int], ages: list[int]) -> int:
        scores = tuple(s for _, s in sorted(zip(ages, scores_), reverse=True))
        n = len(scores)

        dp = [0] * n
        for i in range(n):
            for j in range(i, -1, -1):
                dp[i] = max(dp[i], dp[j] + scores[i]) if scores[i] <= scores[j] else dp[i]
        
        return max(dp)
