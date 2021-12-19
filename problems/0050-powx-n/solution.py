class Solution:
    def myPow(self, x_: float, n_: int) -> float:
        def power(x: float, n: int) -> float:
            if n <= 0: return 1
            p = power(x, n // 2)
            return p * p * (x if n % 2 else 1)
        
        prod = power(x_, abs(n_))
        return  prod if n_ >= 0 else 1 / prod
