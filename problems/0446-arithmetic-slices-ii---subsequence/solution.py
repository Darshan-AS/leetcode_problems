class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [defaultdict(int) for _ in range(n)]
        
        count = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] += dp[j][d] + 1
                count += dp[j][d] # prev value used to ensure slice length >= 3
            
        return count
