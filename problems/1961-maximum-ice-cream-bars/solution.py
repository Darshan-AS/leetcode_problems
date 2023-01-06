class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        return sum(1 for _ in takewhile(lambda x: x <= coins, accumulate(sorted(costs))))
