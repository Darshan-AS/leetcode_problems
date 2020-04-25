class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = j = 0
        
        while i <= j:
            if j >= len(nums) - 1:
                return True
            
            j = max(j, i + nums[i])
            i += 1
        
        return False
