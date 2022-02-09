class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        length = n + 1
        
        prefix_sums = list(accumulate(nums, initial=0))
        mq = deque()
        
        for j in range(n + 1):
            while mq and prefix_sums[j] - prefix_sums[mq[0]] >= k:
                length = min(length, j - mq.popleft())
            
            while mq and prefix_sums[mq[-1]] >= prefix_sums[j]:
                mq.pop()
            
            mq.append(j)
        
        return length if length <= n else -1

