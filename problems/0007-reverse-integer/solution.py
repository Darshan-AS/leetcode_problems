class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return x
        temp = 2 ** 31
        min_int, max_int = - temp, temp - 1
        
        sign = x // abs(x)
        x *= sign
        rev = 0
        while x:
            if rev > max_int // 10 or rev < min_int // 10:
                return 0
            
            rev = rev * 10 + x % 10
            x = x // 10
        return rev * sign
        
