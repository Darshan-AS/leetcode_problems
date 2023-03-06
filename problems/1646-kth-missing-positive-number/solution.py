class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            l, r = (l, m) if arr[m] - (m + 1) >= k else (m + 1, r)
        return l + k

