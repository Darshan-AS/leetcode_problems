class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        n = len(grid[0])
        
        def is_stuck(c: int, row: list[int]) -> bool:
            return (
                c == -1 or
                (1 if c == 0 else row[c - 1], row[c]) == (1, -1) or
                (row[c], -1 if c == n - 1 else row[c + 1]) == (1, -1)
            )
        
        def foo(ball_cols, row):
            return (-1 if is_stuck(c, row) else c + row[c] for c in ball_cols)
        
        return list(reduce(foo, grid, range(n)))
