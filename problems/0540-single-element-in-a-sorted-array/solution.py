class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return functools.reduce(lambda x, y: x ^ y, nums, 0)
