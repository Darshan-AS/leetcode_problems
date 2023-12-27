class Solution:
    def minCost(self, colors: str, needed_time: list[int]) -> int:
        groups = groupby(zip(needed_time, colors), key=itemgetter(1))
        times = (list(next(zip(*g))) for _, g in groups)
        return sum(sum(ts) - max(ts) for ts in times)
        
