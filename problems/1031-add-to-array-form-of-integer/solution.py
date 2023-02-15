class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        def rdigits(n: int) -> Iterable[int]:
            while n: n, r = divmod(n, 10); yield r
        
        def sum_iter(xs: Iterable[int], ys: Iterable[int]) -> Iterable[int]:
            c = 0
            for x, y in zip_longest(xs, ys, fillvalue=0):
                c, s = divmod(x + y + c, 10)
                yield s
            if c: yield c
        
        sum_ = deque()
        sum_.extendleft(sum_iter(reversed(num), rdigits(k)))
        return sum_
