class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        r, c = len(grid), len(grid[0])
        
        def mark_island_as_visited(i, j):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                grid[i][j] = 'v'
                if i + 1 < r and grid[i + 1][j] == "1":
                    stack.append((i + 1, j))
                if j + 1 < c and grid[i][j + 1] == "1":
                    stack.append((i, j + 1))
                if i - 1 >= 0 and grid[i - 1][j] == "1":
                    stack.append((i - 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == "1":
                    stack.append((i, j - 1))
        
        island_count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    island_count += 1
                    mark_island_as_visited(i, j)
        
        return island_count
