class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        prefix_sums = list(accumulate(sorted(nums)))
        return [bisect.bisect(prefix_sums, q) for q in queries]
