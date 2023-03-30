class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def is_scramble(i: int, j: int, n: int) -> bool:            
            return any(
                (is_scramble(i, j        , k) and is_scramble(i + k, j + k, n - k)) or
                (is_scramble(i, j + n - k, k) and is_scramble(i + k, j    , n - k))
                for k in range(1, n)
            ) if n > 1 else s1[i] == s2[j]
        
        return is_scramble(0, 0, len(s1))
