class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda res, x: res ^ x[0] ^ x[1], enumerate(nums), len(nums))
