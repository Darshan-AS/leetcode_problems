class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def is_closed(i: int, j: int) -> bool:
            if i < 0 or j < 0 or i >= m or j >= n: return False
            if grid[i][j] == 1: return True
            grid[i][j] = 1 # mark as visited
            return all(tuple(
                is_closed(i + di, j + dj)
                for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0))
            ))

        return sum(grid[i][j] == 0 and is_closed(i, j) for i, j in product(range(m), range(n)))
