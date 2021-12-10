class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        
        for num in nums:
            if num - 1 in nums_set:
                continue
            
            num_next = num + 1
            while num_next in nums_set:
                num_next += 1
            
            max_length = max(max_length, num_next - num)
        
        return max_length

