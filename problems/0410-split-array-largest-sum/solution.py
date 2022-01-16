class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:        
        def min_splits_with_sum(iterable, max_sum: int) -> int:
            split_count = 1
            curr_sum = 0
            for x in iterable:
                curr_sum += x
                if curr_sum > max_sum:
                    split_count += 1
                    curr_sum = x
            return split_count
        
        low, high = max(nums), sum(nums)
        while low <= high:
            max_sum_allowed = (low + high) // 2
            min_splits = min_splits_with_sum(nums, max_sum_allowed)
            
            if min_splits <= m:
                high = max_sum_allowed - 1
            elif min_splits > m:
                low = max_sum_allowed + 1
        
        return low
