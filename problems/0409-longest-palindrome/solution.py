from functools import reduce
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)
        
        def func(n, x):
            next_n = n + (x - 1 if x % 2 else x)
            return next_n + (1 if not next_n % 2 and x % 2 else 0)
        
        return reduce(func, s_counter.values(), 0)
