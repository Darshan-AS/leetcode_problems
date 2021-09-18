class Solution:
    def rotate(self, nums: List[int], k_: int) -> None:        
        def reverse_inplace(arr: List[int], low: int, high: int) -> None:
            i, j = low, high - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i + 1, j - 1
        
        k = k_ % len(nums)
        reverse_inplace(nums, 0, len(nums))
        reverse_inplace(nums, 0, k)
        reverse_inplace(nums, k, len(nums))
