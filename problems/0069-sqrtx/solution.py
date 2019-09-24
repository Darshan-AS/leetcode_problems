class Solution:
    def mySqrt(self, x: int) -> int:
        # Newton's method
        # a = x
        # while a * a > x:
        #     a = int((a + x / a) / 2)
        # return a
        
        low, high = 0, x
        while True:
            mid = (low + high) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            
            if mid ** 2 > x:
                high = mid - 1
            else:
                low = mid + 1
