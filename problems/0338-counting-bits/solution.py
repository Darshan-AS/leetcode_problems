class Solution:
    def countBits(self, n: int) -> List[int]:
        def counts():
            yield 0
            cs = (1,)
            while True:
                cs1, cs2 = tee(cs, 2)
                yield from cs1
                cs = (c_next for c in cs2 for c_next in (c, c + 1))
        
        return islice(counts(), n + 1)
