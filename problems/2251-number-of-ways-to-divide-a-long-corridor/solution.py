class Solution:
    def numberOfWays(self, corridor: str) -> int:        
        return abs(reduce(mul, starmap(sub, compress(pairwise((i for i, x in enumerate(corridor) if x == 'S')), cycle((0, 1)))), 1)) % 1_000_000_007 if (s := corridor.count('S')) and s % 2 == 0 else 0
