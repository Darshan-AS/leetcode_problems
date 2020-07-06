class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        global_max = local_max = float('-inf')
        for i in A:
            local_max = i + max(local_max, 0)
            global_max = max(global_max, local_max)
        
        global_min = local_min = float('inf')
        for i in A:
            local_min = i + min(local_min, 0)
            global_min = min(global_min, local_min)
        
        global_max_1 = global_max
        global_max_2 = sum(A) - global_min
        return max(global_max_1, global_max_2) if global_max_2 else global_max_1
