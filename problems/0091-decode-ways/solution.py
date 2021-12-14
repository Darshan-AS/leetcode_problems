class Solution:
    def numDecodings(self, s: str) -> int:        
        a, b = 0, 1
        for x in range(len(s)):            
            a, b = b, (
                (b if int(s[x]) else 0) +
                (a if x > 0 and int(s[x - 1]) and int(s[x - 1: x + 1]) <= 26 else 0)
            )
        
        return b
