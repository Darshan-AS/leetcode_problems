class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def bisect_(arr: list, k, reverse: bool = False):            
            left, right = 0, len(arr) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if k < arr[mid]:
                    right = mid - 1
                elif k > arr[mid]:
                    left = mid + 1
                else:
                    left, right = (mid + 1, right) if reverse else (left, mid - 1)
            
            return left
        
        s_nums = sorted(nums)
        # return list(range(bisect.bisect_left(s_nums, target), bisect.bisect_right(s_nums, target)))
        return list(range(bisect_(s_nums, target), bisect_(s_nums, target, reverse=True)))

