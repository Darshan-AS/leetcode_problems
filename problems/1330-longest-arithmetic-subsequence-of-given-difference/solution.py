class Solution:
    def longestSubsequence(self, arr: list[int], d: int) -> int:
        return max(reduce(lambda a, x: setitem(a, x, a.get(x - d, 0) + 1) or a, arr, {}).values())
