class Solution:
    def thirdMax(self, nums: List[int]) -> int:        
        maxes = (-math.inf,) * 3
        
        for num in nums:
            if num > maxes[0]:
                maxes = (num, maxes[0], maxes[1])
            elif maxes[0] > num > maxes[1]:
                maxes = (maxes[0], num, maxes[1])
            elif maxes[1] > num > maxes[2]:
                maxes = (maxes[0], maxes[1], num)
        
        return max(nums) if -math.inf in maxes else maxes[-1]
