from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sl = SortedList(nums[:k])
        maxes = [sl[-1]]
        
        for i in range(k, len(nums)):
            sl.discard(nums[i - k])
            sl.add(nums[i])
            maxes.append(sl[-1])
        
        return maxes
