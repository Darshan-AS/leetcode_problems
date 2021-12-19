class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        visited = {(0, 0)}
        queue = collections.deque([(0, 0, 1)] if grid[0][0] == 0 else [])
        
        while queue:
            i, j, length = queue.popleft()
            if (i, j) == (m - 1, n - 1):
                return length
            
            for di, dj in itertools.product(range(-1, 2), range(-1, 2)):
                next_i, next_j = i + di, j + dj
                if (
                    0 <= next_i < m and 
                    0 <= next_j < n and 
                    grid[next_i][next_j] == 0 and 
                    (next_i, next_j) not in visited
                ):
                    queue.append((next_i, next_j, length + 1))
                    visited.add((next_i, next_j))
        
        return -1
                    
