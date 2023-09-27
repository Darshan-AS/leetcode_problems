class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = reduce(lambda a, x: (a * int(x)) if x.isdigit() else (a + 1), s, 0)

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch.isdigit():
                n //= int(ch)
                k %= n
            else:
                if k == 0 or n == k: return ch 
                n -= 1

