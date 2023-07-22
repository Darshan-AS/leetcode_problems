class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        on_board = lambda i, j: 0 <= i < n and 0 <= j < n
        moves = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
        next_positions = prev_positions = lambda i, j: ((i + di, j + dj) for di, dj in moves)

        @cache
        def on_board_prob(k: int, i: int, j: int) -> float:
            return sum(on_board_prob(k - 1, ni, nj) for ni, nj in next_positions(i, j) if on_board(ni, nj)) / 8 if k else on_board(i, j)
        
        return on_board_prob(k, row, column)
