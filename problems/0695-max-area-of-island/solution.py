class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        seen = set()
        def area_around(r: int, c: int) -> int:
            if not (0 <= r < m and 0 <= c < n and (r, c) not in seen and grid[r][c]):
                return 0
            
            seen.add((r, c))
            return sum(area_around(r + dr, c + dc) for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1))) + 1

        return max(area_around(i, j) for i, j in itertools.product(range(m), range(n)))
