class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        row_diffs = [2 * sum(row) - len(row) for row in grid]
        col_diffs = [2 * sum(col) - len(col) for col in zip(*grid)]
        return [[row_diffs[i] + col_diffs[j] for j in range(len(grid[0]))] for i in range(len(grid))]
        
