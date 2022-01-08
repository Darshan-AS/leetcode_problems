class Solution:
    def mySqrt(self, x: int) -> int:
        # Newton's method
        # a = x
        # while a * a > x:
        #     a = int((a + x / a) / 2)
        # return a
        
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            y = mid * mid
            
            if y > x:
                high = mid - 1
            elif y < x:
                low = mid + 1
            else:
                return mid
        
        return high
