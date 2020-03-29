class Solution:
    def myAtoi(self, s: str) -> int:
        temp = 2 ** 31
        INT_MAX, INT_MIN = temp - 1, - temp
        
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i == len(s):
            return 0
        
        sign = -1 if s[i] == '-' else 1
        i = i + 1 if s[i] in ('+', '-') else i
        
        n = 0
        while i < len(s) and s[i].isdigit():
            n = n * 10 + int(s[i])
            if n * sign > INT_MAX: return INT_MAX
            if n * sign < INT_MIN: return INT_MIN
            i += 1
        
        return n * sign
