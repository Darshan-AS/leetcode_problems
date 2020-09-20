from itertools import product

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        start = end = None
        free_spot_count = 0
        for i, j in product(range(n), range(m)):
            x = grid[i][j]
            if x == 1: start = (i, j)
            elif x == 2: end = (i, j)
            elif x == 0: free_spot_count += 1
        
        def count_paths(i, j, rem):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] in (-1, -2): return 0
            if grid[i][j] == 2: return 0 if rem else 1
            
            grid[i][j] = -2
            path_count = 0
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                path_count += count_paths(i + di, j + dj, rem - 1)
            grid[i][j] = 0
            return path_count
        
        return count_paths(*start, free_spot_count + 1)
