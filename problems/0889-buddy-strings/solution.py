class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b): return False
        
        mismatch = list(filter(lambda x: x[0] != x[1], zip(a, b)))
        if len(mismatch) == 0:
            return len(set(a)) != len(a)
        elif len(mismatch) == 2:
            return mismatch[0] == tuple(reversed(mismatch[1]))
        else:
            return False
