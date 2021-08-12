class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # Iterative version of the previous submission (recursive solution)        
        count_0 = 0
        flips = 0
        for ch in reversed(s):
            if ch == '0':
                count_0 += 1
            else:
                flips = min(count_0, 1 + flips)
        return flips
