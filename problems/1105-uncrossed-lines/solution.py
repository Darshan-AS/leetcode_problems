class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        nums_s, nums_l = sorted((nums1, nums2), key=len)
        m, n = len(nums_s), len(nums_l)
        
        dp = [0] * (m + 1)

        for i in range(n):
            prev = dp[0]
            for j in range(m):
                k = j + 1
                prev, dp[k] = dp[k], (prev + 1 if nums_s[j] == nums_l[i] else max(dp[k], dp[k - 1]))
    
        return dp[-1]
