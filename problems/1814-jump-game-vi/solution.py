from sortedcontainers import SortedList

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        mq = deque() # monotonique (index, max_scores) queue of last k indices
        
        for i, num in enumerate(nums):
            while mq and mq[0][0] < i - k: mq.popleft()
            score = num + (mq[0][1] if mq else 0)
            
            while mq and mq[-1][1] <= score: mq.pop()
            mq.append((i, score))
            
        return mq[-1][1]
