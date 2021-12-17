class Solution:
    def minOperations(self, nums_: List[int], x: int) -> int:
        def max_sub_arr_len(nums: list[int], target: int) -> int:
            i = j = 0
            curr_sum = 0
            max_len = -1
            
            while j < len(nums):
                curr_sum += nums[j]
                
                while i <= j and curr_sum >= target:
                    max_len = max(max_len, j - i + 1) if curr_sum == target else max_len
                    curr_sum -= nums[i]
                    i += 1
                    
                j += 1
            
            return max_len
        
        n = len(nums_)
        s = sum(nums_)
        k = max_sub_arr_len(nums_, s - x) if s != x else 0
        return n - k if k >= 0 else -1
