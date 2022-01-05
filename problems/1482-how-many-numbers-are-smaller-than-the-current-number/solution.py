class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s_nums = sorted(nums)
        s_nums_map = {num: index for index, num in reversed(list(enumerate(s_nums)))}
        
        return [s_nums_map[num] for num in nums]
