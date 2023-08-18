class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        g = reduce(
            lambda g, e: g[e[0]].add(e[1]) or g[e[1]].add(e[0]) or g,
            roads, defaultdict(set),
        )

        rank = lambda u, v: (u != v) * (len(g[u]) + len(g[v]) - (u in g[v]))
        return max(starmap(rank, product(range(n), range(n))))
