class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = -1
        max_num = -math.inf
        is_dominant = True
        
        for i, num in enumerate(nums):
            if max_num < num:
                is_dominant = num >= max_num * 2
                max_index, max_num = i, num
            else:
                is_dominant = is_dominant and max_num >= num * 2
        
        return max_index if is_dominant else -1

