class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
                
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i, j in product(range(target + 1), range(n)):
            dp[i] = dp[i] + (dp[i - nums[j]] if i >= nums[j] else 0)
        
        return dp[-1]
