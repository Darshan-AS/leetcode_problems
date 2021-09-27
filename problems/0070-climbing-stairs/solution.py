from itertools import islice

class Solution:
    def climbStairs(self, n: int) -> int:
        def fib():
            a, b = 1, 1
            yield a
            while True:
                yield b
                a, b = b, a + b
    
        return next(islice(fib(), n, None))
