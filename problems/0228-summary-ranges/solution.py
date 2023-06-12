class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = [[-inf, -inf]]
        for x in nums:
            if x == ranges[-1][1] + 1: ranges[-1][1] = x
            else: ranges.append([x, x])

        return [f'{a}' if a == b else f'{a}->{b}' for a, b in islice(ranges, 1, None)]
