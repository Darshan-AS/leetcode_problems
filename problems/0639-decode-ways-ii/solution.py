class Solution:
    def numDecodings(self, s: str) -> int:
        M = 1_000_000_007
        
        n = len(s)
        a, b = 0, 1
        
        for x in range(n):
            i = x + 2
            b_ = b
            
            prev_ch, ch = s[x - 1] if x else '0', s[x]
            
            if ch == '*':
                b = (b * 9) % M
                if prev_ch == '1':
                    b = (b + a * 9) % M
                elif prev_ch == '2':
                    b = (b + a * 6) % M
                elif prev_ch == '*':
                    b = (b + a * 15) % M
            else:
                b = b if ch != '0' else 0
                if prev_ch == '1':
                    b = (b + a) % M
                elif prev_ch == '2':
                    b = (b + a * (1 if ch <= '6' else 0)) % M
                elif prev_ch == '*':
                    b = (b + a * (2 if ch <= '6' else 1)) % M
            
            a, b = b_, b
        
        return b
