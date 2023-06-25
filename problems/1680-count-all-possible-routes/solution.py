class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        return (routes := cache(lambda s, f: ((s == finish) + sum(routes(e, f - d) for e in range(len(locations)) if s != e and (d := abs(locations[s] - locations[e])) <= f)) % 1_000_000_007))(start, fuel)
