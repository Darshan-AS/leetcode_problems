class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect_(arr: list, k, reverse: bool = False):            
            left, right = 0, len(arr)
            
            while left < right:
                mid = (left + right) // 2
                if k < arr[mid]:
                    right = mid
                elif k > arr[mid]:
                    left = mid + 1
                else:
                    left, right = (mid + 1, right) if reverse else (left, mid)
            
            return left
        
        # start, end = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1
        start, end = bisect_(nums, target), bisect_(nums, target, reverse=True) - 1
        return [start, end] if start <= end else [-1, -1]
