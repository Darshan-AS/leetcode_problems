class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        return reduce(xor, nums)
