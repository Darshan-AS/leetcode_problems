class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for index, value in enumerate(nums):
            if value in seen and index - seen[value] <= k:
                return True
            
            seen[value] = index
        
        return False
