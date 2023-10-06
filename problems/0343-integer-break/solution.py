class Solution:
    def integerBreak(self, n: int) -> int:
        q, r = divmod(n, 3)
        return (
            3 ** q,             # r = 0
            3 ** (q - 1) * 4,   # r = 1
            3 ** q * 2,         # r = 2
        )[r] if n > 3 else (n - 1)
