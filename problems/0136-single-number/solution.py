class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_num = 0
        for i in nums: unique_num ^= i
        return unique_num
