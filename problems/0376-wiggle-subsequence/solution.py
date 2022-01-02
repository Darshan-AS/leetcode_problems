class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [(0, 0)] * n
        dp[0] = (1, 1)
        
        for i in range(1, n):
            pos_max, neg_max = dp[i - 1]
            
            if nums[i - 1] < nums[i]:
                dp[i] = (neg_max + 1, neg_max)
            elif nums[i - 1] > nums[i]:
                dp[i] = (pos_max, pos_max + 1)
            else:
                dp[i] = (pos_max, neg_max)
        
        return max(dp[-1])
