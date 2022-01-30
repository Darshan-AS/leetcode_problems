from sortedcontainers import SortedList

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dq = deque()      # max_scores of last k indices
        sl = SortedList() # sorted max_scores of last k indices
        
        for i, num in enumerate(nums):
            score = num + (sl[-1] if sl else 0)
            dq.append(score)
            sl.add(score)
            
            if i >= k: sl.discard(dq[0]); dq.popleft()
        
        return dq[-1]
