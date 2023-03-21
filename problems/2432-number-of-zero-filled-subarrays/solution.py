class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        lefts = accumulate(enumerate(nums), lambda a, x: x[0] if x[1] else a, initial=-1)
        rights = range(-1, len(nums))
        return sum(map(sub, rights, lefts))
