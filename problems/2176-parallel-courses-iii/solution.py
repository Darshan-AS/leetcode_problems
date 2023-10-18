class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        g = defaultdict(list)
        for pre, nxt in relations: g[pre].append(nxt)

        @cache
        def min_time(x: int) -> int:
            return max(map(min_time, g[x]), default=0) + time[x - 1]

        return max(map(min_time, range(1, n + 1)))
