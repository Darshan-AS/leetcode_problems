class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for i in nums:
            if not count:
                candidate = i
            
            count += 1 if candidate == i else -1
        
        return candidate
