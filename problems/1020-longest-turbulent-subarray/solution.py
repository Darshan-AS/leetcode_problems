from numbers import Real

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def pairwise(iterable):
            a, b = tee(iterable)
            next(b, None)
            return zip(a, b)
        
        def signum(n: Real):
            if n > 0: return +1
            elif n < 0: return -1
            else: return 0
            
        signdiff = (signum(a - b) for a, b in pairwise(arr))
        
        max_len = 0
        curr_len = 0
        prev = -1
        for x in signdiff:
            curr_len = curr_len + 1 if x == -prev else 1
            prev = x
            max_len = max(max_len, curr_len) if x != 0 else max_len
        
        return max_len + 1
