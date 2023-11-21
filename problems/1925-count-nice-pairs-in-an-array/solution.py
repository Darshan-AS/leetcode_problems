class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        return sum(
            (n - 1) * n // 2 % 1_000_000_007
            for n in Counter(x - int(str(x)[::-1]) for x in nums).values()
        ) % 1_000_000_007
