from functools import cache


class Solution:
    
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:       
        @cache
        def count_paths(move: int, r: int, c: int) -> int:
            if not (0 <= r < m and 0 <= c < n):
                return 1

            if move == 0:
                return 0

            return sum(
                count_paths(move - 1, r + dr, c + dc)
                for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1))
            ) % 1_000_000_007

        return count_paths(maxMove, startRow, startColumn)
