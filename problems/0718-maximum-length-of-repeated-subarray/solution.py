class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        
        dp = [0] * (n2 + 1)
        prev = 0
        max_len = 0
        for i, j in product(range(n1), range(n2)):
            x = j + 1
            prev = prev if j else dp[0]
            prev, dp[x] = dp[x], prev + 1 if nums1[i] == nums2[j] else 0
            max_len = max(max_len, dp[x])
        
        return max_len
