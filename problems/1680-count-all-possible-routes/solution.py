class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        @cache
        def routes(s: int, f: int) -> int:
            return ((s == finish) + sum(routes(e, f - d) for e in range(len(locations)) if s != e and (d := abs(locations[s] - locations[e])) <= f)) % 1_000_000_007
        
        return routes(start, fuel)
