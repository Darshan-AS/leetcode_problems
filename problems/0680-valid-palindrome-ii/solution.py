class Solution:
    def validPalindrome(self, s: str) -> bool:
        def strip_eq(p: str, i: int = 0, j: int = None):
            j = len(s) - 1 if j is None else j
            
            while i <= j and p[i] == p[j]:
                i, j = i + 1, j - 1
            
            return i, j
        
        start, end = strip_eq(s)
        ps = ((start, end), strip_eq(s, start + 1, end), strip_eq(s, start, end - 1))
        return any(starmap(operator.gt, ps))
        
