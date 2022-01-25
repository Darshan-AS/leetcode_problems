class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = math.inf
        
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True
        
        return False
