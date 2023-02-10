class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ones = tuple((i, j, 0) for i, j in product(range(m), range(n)) if grid[i][j])

        in_bounds = lambda i, j: 0 <= i < n and 0 <= j < m

        d = 0
        queue = deque(ones)
        seen = set(ones)
        while queue:
            i, j, d = queue.popleft()
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + di, j + dj
                if in_bounds(ni, nj) and (ni, nj) not in seen and grid[ni][nj] == 0:
                    seen.add((ni, nj))
                    queue.append((ni, nj, d + 1))
        return d if d else -1
