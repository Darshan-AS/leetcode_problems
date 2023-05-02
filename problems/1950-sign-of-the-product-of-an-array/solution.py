class Solution:
    def arraySign(self, nums: list[int]) -> int:
        return reduce(mul, map(lambda x: (x > 0) - (x < 0), nums))
