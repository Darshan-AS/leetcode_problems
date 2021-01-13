class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p_ans = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            p1, p2, ans = (p1-1, p2, nums1[p1]) if nums1[p1] > nums2[p2] else (p1, p2-1, nums2[p2])
            nums1[p_ans] = ans
            p_ans -= 1
        if p2 >= 0:
            nums1[:p_ans + 1] = nums2[:p2 + 1]
