class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        def count_paths(start: tuple[int, int], end: tuple[int, int], empty_counts: int, seen: set=None) -> int:
            seen = seen if seen else set()
            x, y = start
            if x < 0 or x >= m or y < 0 or y >= n or start in seen or grid[x][y] == -1:
                return 0
            
            seen.add(start)
            
            path_count = sum(
                count_paths((x + dx, y + dy), end, empty_counts - 1, seen)
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1))
            ) if start != end else (0 if empty_counts else 1)
            
            seen.remove(start)
            
            return path_count
        
        
        m, n = len(grid), len(grid[0])
        start_ = end_ = (0, 0)
        empty_counts_ = 1 # Include start
        for i, j in product(range(m), range(n)):
            x = grid[i][j]
            if x == 1: start_ = (i, j)
            elif x == 2: end_ = (i, j)
            elif x == 0: empty_counts_ += 1
        
        return count_paths(start_, end_, empty_counts_)
