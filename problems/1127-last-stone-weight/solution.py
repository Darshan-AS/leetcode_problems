class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        hq = list(map(neg, stones))
        heapify(hq)

        while len(hq) > 1 and hq[0] != 0:
            heappush(hq, heappop(hq) - heappop(hq))
        
        return -heappop(hq)
