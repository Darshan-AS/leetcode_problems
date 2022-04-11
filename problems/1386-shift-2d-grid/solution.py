class Solution:
    def shiftGrid(self, grid: list[list[int]], k_: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        t = m * n
        k = k_ % t
        
        initial_nums = chain.from_iterable(grid)
        shifted_nums = islice(cycle(initial_nums), t - k, t - k + t)
        
        return [list(islice(shifted_nums, n)) for _ in range(m)]
        
