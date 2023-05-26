class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        @cache
        def f(p, i, m):
            if i == n: return 0
            res = inf if p == 1 else -1
            s = 0
            for x in range(1, min(2 * m, n - i) + 1):
                s += piles[i + x - 1]
                res = min(res, f(0, i + x, max(m, x))) if p else max(res, s + f(1, i + x, max(m, x)))
            return res
        
        return f(0, 0, 1)
