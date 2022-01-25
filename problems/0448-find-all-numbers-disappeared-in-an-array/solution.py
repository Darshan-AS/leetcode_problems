class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for num in nums:
            x = abs(num)
            nums[x - 1] = -abs(nums[x - 1])
                
        disappeared = []
        for i in range(n):
            if nums[i] > 0:
                disappeared.append(i + 1)
            nums[i] = abs(nums[i])
        
        return disappeared
