class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = defaultdict(int, {0: 0})

        for r in rods:
            dp_ = dp.copy()
            for d, t in dp.items():
                s = t - d
                dp_[d + r] = max(dp_[d + r], t + r)
                dp_[abs(s + r - t)] = max(dp_[abs(s + r - t)], max(s + r, t))
            dp = dp_
        
        return dp[0]

