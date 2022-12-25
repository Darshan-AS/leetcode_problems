class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        return map(
            bisect.bisect,
            repeat(list(accumulate(sorted(nums)))),
            queries,
        )
