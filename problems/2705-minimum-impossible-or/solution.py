class Solution:
    def minImpossibleOR(self, nums: list[int]) -> int:
        nums_set = set(nums)
        powers_of_2 = accumulate(repeat(2), mul, initial=1)
        return next(dropwhile(lambda n: n in nums_set, powers_of_2))
