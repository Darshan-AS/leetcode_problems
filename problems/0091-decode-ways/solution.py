class Solution:
    def numDecodings(self, s: str) -> int:
        a, b, p_ch = 0, 1, ''
        for ch in s:
            a, b, p_ch = b, b * (int(ch) > 0) + a * (10 <= int(p_ch + ch) <= 26), ch
        return b
