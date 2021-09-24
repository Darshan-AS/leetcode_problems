class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        rotten_set = set()
        
        for i, j in itertools.product(range(m), range(n)):
            x = grid[i][j]
            if x == 1: fresh_count += 1
            if x == 2: rotten_set.add((i, j))
        
        minutes = 0
        while rotten_set and fresh_count:
            next_rotten_set = set()
            for i, j in rotten_set:
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    i_, j_ = i + di, j + dj
                    if 0 <= i_ < m and 0 <= j_ < n and grid[i_][j_] == 1:
                        grid[i_][j_] = 2
                        fresh_count -= 1
                        next_rotten_set.add((i_, j_))
            rotten_set = next_rotten_set
            minutes += 1
        
        return minutes if fresh_count == 0 else -1
