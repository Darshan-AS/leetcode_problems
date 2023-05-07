class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        return len(reduce(lambda a, x: (
            a.append(x)
            if not a or a[-1] < x else
            a.__setitem__(bisect.bisect_left(a, x), x)
        ) or a, nums, []))
