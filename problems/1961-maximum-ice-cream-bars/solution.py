class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs_hq = list(costs)
        heapify(costs_hq)

        bars = 0
        while costs_hq and coins >= costs_hq[0]:
            coins -= heappop(costs_hq)
            bars += 1
        
        return bars
