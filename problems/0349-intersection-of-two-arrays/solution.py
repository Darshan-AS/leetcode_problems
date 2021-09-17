class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list(set(nums1) & set(nums2))
        return list(set(i for i in nums2 if i in set(nums1)))
