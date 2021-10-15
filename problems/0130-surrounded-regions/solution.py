class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def replace_all(old: str, new: str):
            for i, j in itertools.product(range(m), range(n)):
                board[i][j] = new if board[i][j] == old else board[i][j]
        
        def replace_region(i: int, j: int, old: str, new: str):
            if board[i][j] != old: return
            board[i][j] = new
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                next_i, next_j = i + di, j + dj
                if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] == old:
                    replace_region(next_i, next_j, old, new)
        
        replace_all('O', 'Y')
        for i, j in itertools.chain(
            ((0, j) for j in range(n)),
            ((i, n - 1) for i in range(1, m)),
            ((m - 1, j) for j in range(n - 2, -1, -1)),
            ((i, 0) for i in range(m - 2, 0, -1))
        ): replace_region(i, j, 'Y', 'O')
        replace_all('Y', 'X')
