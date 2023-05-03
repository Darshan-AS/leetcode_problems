class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        return (lambda a, b: [a - b, b - a])(set(nums1), set(nums2))
