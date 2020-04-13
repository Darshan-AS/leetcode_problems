class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen_map = {0: -1}
        max_length = count = 0
        
        for index, ele in enumerate(nums):
            count += 1 if ele else -1
            if count in seen_map.keys():
                max_length = max(max_length, index - seen_map[count])
            else:
                seen_map[count] = index
        
        return max_length
