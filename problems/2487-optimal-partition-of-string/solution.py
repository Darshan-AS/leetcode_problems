class Solution:
    def partitionString(self, s: str) -> int:
        return reduce(
            lambda a, x: (x, a[1] + 1) if a[0] & x else (a[0] | x, a[1]),
            map(lambda c: 1 << (ord(c) - ord('a')), s),
            (0, 1), # (seen bit mask, count)
        )[1]

