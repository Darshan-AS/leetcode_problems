from itertools import islice

class Solution:
    def fib(self, n: int) -> int:
        def fib_():
            a, b = 0, 1
            while True:
                yield a
                a, b = b, a + b
        
        return next(islice(fib_(), n, None))
