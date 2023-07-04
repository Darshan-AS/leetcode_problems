class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        def counts(a: tuple[int, int], num: int) -> tuple[int, int]:
            ones, twos = a
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
            return ones, twos
        
        return reduce(counts, nums, (0, 0))[0]
