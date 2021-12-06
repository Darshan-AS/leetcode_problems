class Solution:
    def findIntegers(self, n: int) -> int:
        def fib():
            a, b = 1, 2
            while True:
                yield a
                a, b = b, a + b
                
        i = int(log(n, 2))
        fibs = list(islice(fib(), i + 1))

        prev_bit = 0
        sum_ = 0
        while i >= 0:
            bit = n & (1 << i)
            if bit:
                sum_ += fibs[i]
                if prev_bit:
                    sum_ -= 1
                    break
            i -= 1
            prev_bit = bit
        
        return sum_ + 1
