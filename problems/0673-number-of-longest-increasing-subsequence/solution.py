class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [(0, 0)] * n
        dp[0] = (1, 1)

        for i in range(1, n):
            length = max((dp[j][0] for j in range(i) if nums[j] < nums[i]), default=0)
            dp[i] = (1 + length, max(sum(dp[j][1] for j in range(i) if nums[j] < nums[i] and dp[j][0] == length), 1))
            
        length = max(dp)[0]
        return sum(c for l, c in dp if l == length)
