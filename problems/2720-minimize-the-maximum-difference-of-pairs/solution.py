class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        diffs = tuple(abs(a - b) for a, b in pairwise(sorted(nums)))

        count_pairs = lambda max_d: sum(accumulate(
                map(le, diffs, repeat(max_d)),
                lambda a, x: not a and x,
                initial=False,
            ))
        
        l, r = 0, max(diffs, default=0)
        while l < r:
            m = (l + r) // 2
            l, r = (m + 1, r) if count_pairs(m) < p else (l, m)
        return l
