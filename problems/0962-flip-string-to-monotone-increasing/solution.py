class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        return reduce(lambda a, x: (
                (a[0], a[1] + 1)
                if x == '1'
                else (min(a[0] + 1, a[1]), a[1])
            ), s, (0, 0), # (min_flips, prefix_1s)
        )[0]

