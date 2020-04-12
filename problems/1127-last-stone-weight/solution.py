import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_ = list(map(lambda x: -x, stones))
        heapq.heapify(stones_)
        
        while(len(stones_) > 1):
            a = heapq.heappop(stones_)
            b = heapq.heappop(stones_)
            heapq.heappush(stones_, a - b)
        
        return -stones_[0]
