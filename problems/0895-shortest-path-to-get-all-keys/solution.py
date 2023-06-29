class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        start = (0, 0)
        for i, s in enumerate(grid):
            for j, ch in enumerate(s):
                if ch == '@':
                    start = (i, j)
                    break
        k = sum(map(str.islower, chain.from_iterable(grid)))
        
        frontier = deque([(start, 0, set())])
        seen = {(indices, frozenset(keys)) for indices, d, keys in frontier}
        while frontier:
            (i, j), d, keys = frontier.popleft()
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + di, j + dj
                if not (0 <= ni < m and 0 <= nj < n) or grid[ni][nj] == '#' or (grid[ni][nj].isupper() and grid[ni][nj].lower() not in keys) or ((ni, nj), frozenset(keys)) in seen: continue
                new_keys = keys | ({grid[ni][nj]} if grid[ni][nj].islower() else set())
                if len(new_keys) == k: return d + 1
                frontier.append(((ni, nj), d + 1, new_keys))
                seen.add(((ni, nj), frozenset(new_keys)))
        return -1

