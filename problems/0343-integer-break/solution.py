class Solution:
    def integerBreak(self, num: int) -> int:
        if num <= 3: return num - 1
        
        q, r = divmod(num, 3)
        
        if r == 0:
            return 3 ** q
        elif r == 1:
            return 3 ** (q - 1) * 4
        elif r == 2:
            return 3 ** q * 2
