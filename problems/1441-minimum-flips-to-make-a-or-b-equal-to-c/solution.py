class Solution:
    def minFlips(self, an: int, bn: int, cn: int) -> int:
        def bin_(n: int) -> Iterator[Literal[0, 1]]:
            while n: yield n & 1; n >>= 1
        
        return sum((not a and not b) if c else (a + b) for a, b, c in zip_longest(bin_(an), bin_(bn), bin_(cn), fillvalue=0))
