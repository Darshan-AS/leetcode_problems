class Solution:
    def countBits(self, n: int) -> list[int]:
        return reduce(lambda a, x: setitem(a, x, a[x // 2] + x % 2) or a, range(n + 1), [0] * (n + 1))

