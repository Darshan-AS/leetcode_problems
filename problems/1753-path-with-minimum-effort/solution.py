class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m, n = len(heights), len(heights[0])
        moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
        start, end = (0, 0), (m - 1, n - 1)

        in_bound = lambda ij: 0 <= ij[0] < m and 0 <= ij[1] < n
        adjacents = lambda i, j: ((i + di, j + dj) for di, dj in moves)

        frontier = [(0, 0, 0)]
        seen = set()
        opt_effort = 0
        
        while frontier:
            effort, i, j = heappop(frontier)
            seen.add((i, j))
            opt_effort = max(opt_effort, effort)
            if (i, j) == end: break

            for ni, nj in filter(in_bound, adjacents(i, j)):
                if (ni, nj) in seen: continue
                heappush(frontier, (abs(heights[i][j] - heights[ni][nj]), ni, nj))
            
        return opt_effort
