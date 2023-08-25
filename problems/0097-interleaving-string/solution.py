class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def interable(i: int, j: int) -> bool:
            return (
                (i < 0 and j < 0) or
                (i >= 0 and s3[i + j + 1] == s1[i] and interable(i - 1, j)) or
                (j >= 0 and s3[i + j + 1] == s2[j] and interable(i, j - 1))
            )
        
        return len(s1) + len(s2) == len(s3) and interable(len(s1) - 1, len(s2) - 1)
