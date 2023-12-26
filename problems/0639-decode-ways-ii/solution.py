class Solution:
    def numDecodings(self, s: str) -> int:
        M = 1_000_000_007

        a, b = 0, 1
        
        for prev_ch, ch in pairwise(chain('0', s)):
            p = q = 0

            # Number of ways considering `prev_ch + ch` as a single number.
            match prev_ch, ch:
                case '1', '*': p = 9
                case '2', '*': p = 6
                case '*', '*': p = 15
                case '1',  _ : p = 1
                case '2',  x : p = 1 if x <= '6' else 0
                case '*',  x : p = 2 if x <= '6' else 1
            
            # Number of ways considering only `ch` as a single number.
            match ch:
                case '*': q = 9
                case '0': q = 0
                case  _ : q = 1
            
            a, b = b, (a * p + b * q) % M
        
        return b
