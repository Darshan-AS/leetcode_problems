class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ixs = (i for i, x in enumerate(corridor) if x == 'S')
        sofa_count = corridor.count('S')
        spot_ranges = compress(pairwise(ixs), cycle((0, 1)))
        ways = abs(reduce(mul, starmap(sub, spot_ranges), 1))
        return ways % 1_000_000_007 if sofa_count and sofa_count % 2 == 0 else 0
