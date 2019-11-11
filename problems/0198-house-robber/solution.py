class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        a, b = nums[0], max(nums[0], nums[1])
        max_rob = 0
        for i in range(2, n):
            max_rob = max(a + nums[i], b)
            a, b = b, max_rob
        
        return max_rob
