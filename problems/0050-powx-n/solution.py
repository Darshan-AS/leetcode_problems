class Solution:
    def myPow(self, x: float, n_: int) -> float:
        p, n = 1, abs(n_)
        while n:
            p, n = (p * x, n - 1) if n % 2 else (p, n)
            x, n = x * x, n // 2
        return p if n_ >= 0 else 1 / p
