class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def max_uncrossed_lines(i, j):
            return (
                max_uncrossed_lines(i - 1, j - 1) + 1
                if nums1[i] == nums2[j] else 
                max(max_uncrossed_lines(i - 1, j), max_uncrossed_lines(i, j - 1))
            ) if i >= 0 and j >= 0 else 0
        
        return max_uncrossed_lines(len(nums1) - 1, len(nums2) - 1)
