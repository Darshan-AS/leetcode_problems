class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return x
        temp = 2 ** 31
        min_int, max_int = - temp, temp - 1
        
        sign = x // abs(x)
        rev = int(str(abs(x))[::-1]) * sign
        
        if rev > max_int or rev < min_int:
            return 0
        return rev
