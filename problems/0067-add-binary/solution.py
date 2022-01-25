class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_ = []
        c = 0
        
        for x, y in zip_longest(map(int, reversed(a)), map(int, reversed(b)), fillvalue=0):
            s, c = x ^ y ^ c, (x & y) | (y & c) | (c & x)
            sum_.append(s)
        if c: sum_.append(c)
            
        return ''.join(map(str, reversed(sum_)))
