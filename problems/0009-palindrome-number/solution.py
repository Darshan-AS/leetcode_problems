class Solution:
    def isPalindrome(self, x: int) -> bool:
        def rev_digits(n: int) -> Iterator[int]:
            while n:
                yield n % 10
                n //= 10
        
        def undigits(ints: Iterable[int]) -> int:
            n = 0
            for i in ints:
                n = n * 10 + i
            return n
        
        return x == undigits(rev_digits(abs(x)))
