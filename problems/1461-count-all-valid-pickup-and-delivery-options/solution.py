class Solution:
    @cache
    def countOrders(self, n: int) -> int:
        return (self.countOrders(n - 1) * (2 * n - 1) * (2 * n) // 2) % 1_000_000_007 if n else 1
