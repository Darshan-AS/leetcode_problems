class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max, curr_min = float('-inf'), float('inf')
        global_max = curr_max
        
        for i in nums:
            curr_max, curr_min = (
                max(i, curr_max * i if i > 0 else curr_min * i),
                min(i, curr_min * i if i > 0 else curr_max * i)
            )
            global_max = max(global_max, curr_max)
        
        return global_max
