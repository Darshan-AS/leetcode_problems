class Solution:
    def countGoodStrings(self, l: int, h: int, zero: int, one: int) -> int:
        return (f := cache(lambda n: n <= h and ((n >= l) + f(n + zero) + f(n + one)) % 1_000_000_007))(0)
