class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        dp = [0] * (n + 1)
        for i, j in product(range(m), range(n)):
            prev = prev if j > 0 else 0
            prev, dp[j + 1] = dp[j + 1], prev + 1 if nums1[i] == nums2[j] else max(dp[j + 1], dp[j])
        
        return dp[-1]
