class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        make_range = lambda a, x: (setitem(a[-1], 1, x) if x == a[-1][1] + 1 else a.append([x, x])) or a
        ranges = reduce(make_range, nums, [[-inf, -inf]])
        return [f'{a}' if a == b else f'{a}->{b}' for a, b in islice(ranges, 1, None)]
