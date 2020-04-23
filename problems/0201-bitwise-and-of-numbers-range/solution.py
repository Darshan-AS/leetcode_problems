class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0 or m == n: 
            return m
        
        return n & m & (-1 << ceil(log(n - m, 2)))
        
