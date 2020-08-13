from itertools import product
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_queue = deque()
        fresh_count = 0
        
        m, n = len(grid), len(grid[0])
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                fresh_count += 1
            elif grid[i][j] == 2:
                rotten_queue.append((i, j))
        
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        minutes = 0
        while rotten_queue and fresh_count:
            for _ in range(len(rotten_queue)):
                rot_i, rot_j = rotten_queue.popleft()
                for di, dj in dirs:
                    i, j = rot_i + di, rot_j + dj
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh_count -= 1
                        rotten_queue.append((i, j))
            minutes += 1
        
        return -1 if fresh_count else minutes
