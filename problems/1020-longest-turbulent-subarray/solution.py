class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_count = 1
        end_low, end_high = 1, 1
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                end_low, end_high = end_high + 1, 1
            elif arr[i - 1] < arr[i]:
                end_low, end_high = 1, end_low + 1
            else:
                end_low, end_high = 1, 1
            
            max_count = max(max_count, end_low, end_high)
        return max_count
            
