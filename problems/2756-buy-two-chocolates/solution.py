class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        return z if  (z := money - sum(reduce(lambda a, x: (x, a[0]) if x < a[0] else (a[0], min(a[1], x)), prices, (inf, inf)))) >= 0 else money
