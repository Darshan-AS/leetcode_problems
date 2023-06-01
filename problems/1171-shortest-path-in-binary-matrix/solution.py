class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        start, end = (0, 0), (n - 1, n - 1)

        # Helper functions
        in_bound = lambda cell: 0 <= cell[0] < n and 0 <= cell[1] < n
        grid_get = lambda cell: grid[cell[0]][cell[1]] if in_bound(cell) else 1
        all_nbrs = lambda cell: product(range(cell[0] - 1, cell[0] + 2), range(cell[1] - 1, cell[1] + 2))
        is_clear = lambda cell, skips: grid_get(cell) == 0 and cell not in skips

        if start == end: return -1 if grid_get(start) else 1
        queue = deque([] if grid_get(start) else [(start, 1)])
        seen = {start}
        valid_nbr = partial(is_clear, skips=seen)

        while queue:
            cell, length = queue.popleft()
            valid_nbrs = set(filter(valid_nbr, all_nbrs(cell)))

            if end in valid_nbrs: return length + 1
            queue.extend(zip(valid_nbrs, repeat(length + 1)))
            seen.update(valid_nbrs)
        
        return -1
