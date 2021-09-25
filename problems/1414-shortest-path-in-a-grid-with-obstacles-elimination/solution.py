from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k_: int) -> int:
        m, n = len(grid), len(grid[0])
        if k_ > (min_steps := m + n - 2): return min_steps
        
        seen = {(0, 0, k_)}
        queue = deque([(0, 0, 0, k_)])
        while queue:
            curr_i, curr_j, steps, k = queue.popleft()
            if (curr_i, curr_j) == (m - 1, n - 1):
                return steps
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                i, j = curr_i + di, curr_j + dj
                if 0 <= i < m and 0 <= j < n and (i, j, k) not in seen and k - grid[i][j] >= 0:
                    seen.add((i, j, k))
                    queue.append((i, j, steps + 1, k - grid[i][j]))
        
        return -1
