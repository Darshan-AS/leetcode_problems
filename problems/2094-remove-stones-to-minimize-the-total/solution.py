class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        piles_hq = list(map(neg, piles))
        heapify(piles_hq)

        for _ in range(k):
            n = -heappop(piles_hq)
            heappush(piles_hq, -(n - n // 2))
        
        return -sum(piles_hq)
