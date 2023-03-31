class Solution:
    def ways(self, pizza: list[str], k_: int) -> int:
        m, n = len(pizza), len(pizza[0])

        @cache
        def apples(r: int, c: int) -> int:
            return (pizza[r][c] == 'A') + apples(r + 1, c) + apples(r, c + 1) - apples(r + 1, c + 1) if 0 <= r < m and 0 <= c < n else 0

        @cache
        def ways_(r: int, c: int, k: int) -> int:
            if apples(r, c) == 0: return 0
            if k == 1: return 1

            h_ways = sum(ways_(i, c, k - 1) for i in range(r + 1, m) if apples(r, c) - apples(i, c))
            v_ways = sum(ways_(r, i, k - 1) for i in range(c + 1, n) if apples(r, c) - apples(r, i))
            
            return (h_ways + v_ways) % 1_000_000_007
        
        return ways_(0, 0, k_)
