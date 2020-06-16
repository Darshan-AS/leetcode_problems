class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        
        while left <= right:
            mid = (left + right) // 2
            
            mid2 = mid * mid
            if mid2 == num:
                return True
            elif mid2 < num:
                left = mid + 1
            elif mid2 > num:
                right = mid - 1
        
        return False
