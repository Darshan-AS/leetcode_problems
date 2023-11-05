class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        maxes = islice(accumulate(arr, max), 1, None)
        winners = (x for x, g in groupby(maxes) if sum(1 for _ in g) >= k)
        return next(winners, max(arr))
