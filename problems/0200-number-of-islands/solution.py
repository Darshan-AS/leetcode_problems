class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def mark_island_as_visited(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] in ('v', '0'): return
            
            grid[i][j] = 'v'
            mark_island_as_visited(i + 1, j)
            mark_island_as_visited(i - 1, j)
            mark_island_as_visited(i, j + 1)
            mark_island_as_visited(i, j - 1)
        
        num_islands = 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] == "1":
                mark_island_as_visited(i, j)
                num_islands += 1
        
        return num_islands
