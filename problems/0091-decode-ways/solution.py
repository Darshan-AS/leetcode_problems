class Solution:
    def numDecodings(self, s: str) -> int:
        return reduce(
            lambda a, x: (x, a[2], a[2] * (int(x) > 0) + a[1] * (10 <= int(a[0] + x) <= 26)),
            s, ('', 0, 1), # (prev_char, ways[i - 2], ways[i - 1])
        )[2]
