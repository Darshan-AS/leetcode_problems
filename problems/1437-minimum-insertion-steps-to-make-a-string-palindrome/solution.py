class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def min_inserts(i: int, j: int) -> int:
            return (
                min_inserts(i + 1, j - 1)
                if s[i] == s[j]
                else 1 + min(min_inserts(i, j - 1), min_inserts(i + 1, j))
            ) if i < j else 0
        
        return min_inserts(0, len(s) - 1)
