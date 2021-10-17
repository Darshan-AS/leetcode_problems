class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums_counter = collections.Counter(nums)
        
        power_set = [[]]
        for num in nums_counter:
            power_set.extend([p + [num] * count for p in power_set for count in range(1, nums_counter[num] + 1)])
        
        return power_set
