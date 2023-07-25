class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2
            l, r = (m + 1, r) if arr[m] < arr[m + 1] else (l, m)
        return l
