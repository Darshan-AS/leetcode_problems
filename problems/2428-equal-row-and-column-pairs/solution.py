class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        return sum(starmap(eq, product(grid, list(map(list, zip(*grid))))))
