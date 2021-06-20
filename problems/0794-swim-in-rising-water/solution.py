from queue import PriorityQueue


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        is_in_bound = lambda p: 0 <= p[0] < m and 0 <= p[1] < n
        get_adjacent_points = lambda p: (
            (p[0] + dr, p[1] + dc) for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1))
        )
        make_point = (
            lambda p: (grid[p[0]][p[1]], p[0], p[1]) if is_in_bound(p) else (-1, -1, -1)
        )

        start_point, end_point = make_point((0, 0)), make_point((m - 1, n - 1))

        pq = PriorityQueue()
        pq.put(start_point)

        max_time = 0
        visited_points = set()
        while not pq.empty():
            e, i, j = pq.get()

            visited_points.add((i, j))
            max_time = max(max_time, e)

            if (e, i, j) == end_point:
                return max_time

            for p in get_adjacent_points((i, j)):
                if is_in_bound(p) and p not in visited_points:
                    pq.put(make_point(p))

        return max_time
