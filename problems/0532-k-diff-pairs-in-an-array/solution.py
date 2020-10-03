from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:        
        counter = Counter(nums)
        return sum(counter[n + k] > (k == 0) for n in counter)
