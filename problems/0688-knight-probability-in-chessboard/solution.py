class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        on_board = lambda i, j: 0 <= i < n and 0 <= j < n
        moves = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
        next_positions = prev_positions = lambda i, j: ((i + di, j + dj) for di, dj in moves)

        next_probs = lambda prob, k: [[sum(prob[ni][nj] for ni, nj in next_positions(i, j) if on_board(ni, nj)) / 8 for j in range(n)] for i in range(n)]
        probs = reduce(next_probs, range(1, k + 1), [[1] * n for _ in range(n)])
        
        return probs[row][column]
