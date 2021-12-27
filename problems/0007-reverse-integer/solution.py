class Solution:
    def reverse(self, x: int) -> int:
        def digits(n: int) -> Iterator[int]:
            while n:
                yield n % 10
                n = n // 10
        
        def undigits(ints: Iterator[int], max_n: int = None) -> int:
            n = 0
            for i in ints:
                if n > (max_n - i) // 10: return 0
                n = (n * 10) + i
            return n
        
        return undigits(digits(abs(x)), max_n=2 ** 31) * (1 if x >= 0 else -1)
        
