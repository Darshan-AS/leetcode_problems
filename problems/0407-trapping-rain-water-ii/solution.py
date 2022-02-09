class Solution:
    def trapRainWater(self, heights: list[list[int]]) -> int:
        m, n = len(heights), len(heights[0])
        boundaries = chain(
            zip(repeat(0), range(n - 1)),
            zip(range(m - 1), repeat(n - 1)),
            zip(repeat(m - 1), range(n - 1, 0, -1)),
            zip(range(m - 1, 0, -1), repeat(0))
        )
        
        is_inbound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        seen = set(boundaries)
        pq = [(heights[i][j], (i, j)) for i, j in seen]
        heapify(pq)
        
        max_h = 0
        water_units = 0
        
        while pq:
            h, (i, j) = heappop(pq)
            max_h = max(max_h, h)
            water = max_h - h
            water_units += water
            
            adj = (
                (heights[i_][j_], (i_, j_))
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0))
                if (i_ := i + di, j_ := j + dj) not in seen and is_inbound(i_, j_)
            )
            
            for h, ij in adj: seen.add(ij); heappush(pq, (h, ij))
        
        return water_units
