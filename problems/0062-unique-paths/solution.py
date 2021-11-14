class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def paths(i: int, j: int) -> int:
            if i == 0 and j == 0: return 1
            return paths(i - 1, j) + paths(i, j - 1) if 0 <= i < m and 0 <= j < n else 0
        
        return paths(m - 1, n - 1)
