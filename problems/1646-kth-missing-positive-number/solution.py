class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] > k + mid:
                end = mid - 1
            else:
                start = mid + 1
        return k + start
