class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for index, val in enumerate(arr):
            if val > k + index:
                return k + index
        return k + len(arr)
