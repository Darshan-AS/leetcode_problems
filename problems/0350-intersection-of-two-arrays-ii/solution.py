class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return (Counter(nums1) & Counter(nums2)).elements()
        nums1_counter = collections.Counter(nums1)
        
        intersection = []
        for i in nums2:
            if nums1_counter[i]:
                intersection.append(i)
                nums1_counter[i] -= 1
        
        return intersection
