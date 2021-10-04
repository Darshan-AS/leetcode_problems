class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        for i, j in itertools.product(range(m), range(n)):
            if grid[i][j]:
                count += 4
                if i > 0 and grid[i - 1][j]:
                    count -= 2
                if j > 0 and grid[i][j - 1]:
                    count -=2
        return count
            
