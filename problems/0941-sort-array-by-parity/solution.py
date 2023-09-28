class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]        
