class Solution:
    def integerBreak(self, n: int) -> int:
        return (
            3 ** (n // 3),
            3 ** (n // 3 - 1) * 4,
            3 ** (n // 3) * 2,
        )[n % 3] if n > 3 else (n - 1)
