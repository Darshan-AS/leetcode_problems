class Solution:
    def findMedianSortedArrays(self, nums_a: list[int], nums_b: list[int]) -> float:
        nums1, nums2 = sorted((nums_a, nums_b), key=len)
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = total // 2
        
        low1, high1 = 0, n1 - 1
        while True:
            mid1 = (low1 + high1) // 2
            mid2 = half - mid1 - 2
            
            x1 = nums1[mid1] if mid1 >= 0 else -math.inf
            y1 = nums1[mid1 + 1] if mid1 + 1 < n1 else math.inf
            
            x2 = nums2[mid2] if mid2 >= 0 else -math.inf
            y2 = nums2[mid2 + 1] if mid2 + 1 < n2 else math.inf
                        
            if x1 > y2: high1 = mid1 - 1
            elif x2 > y1: low1 = mid1 + 1
            else: return min(y1, y2) if total % 2 else (max(x1, x2) + min(y1, y2)) / 2
