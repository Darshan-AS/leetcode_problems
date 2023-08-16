class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = deque()
        maxes = []
        
        for i in range(len(nums)):            
            if mq and mq[0] <= i - k: mq.popleft()
            while mq and nums[mq[-1]] <= nums[i]: mq.pop()
            
            mq.append(i)
            if i >= k - 1: maxes.append(nums[mq[0]])
        
        return maxes
