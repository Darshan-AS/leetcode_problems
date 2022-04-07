class Solution:
    def lastStoneWeight(self, stones_: list[int]) -> int:
        stones = list(map(operator.neg, stones_))
        heapq.heapify(stones)
        
        while len(stones) > 1 and stones[0] != 0:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            heapq.heappush(stones, a - b)
        
        return -stones[0]
