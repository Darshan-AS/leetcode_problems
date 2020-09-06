class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes_count, i = 0, n
        while i := i // 5: zeroes_count += i
        return zeroes_count
