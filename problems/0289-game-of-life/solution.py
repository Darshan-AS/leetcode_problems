class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        
        def will_be_alive(alive: bool, live_neighbours_count: int):
            return (live_neighbours_count == 2 and alive) or (live_neighbours_count == 3)
        
        def get_neighbours(r: int, c: int) -> list[tuple[int, int]]:
            return [
                (nr, nc)
                for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
                if 0 <= (nr := r + dr) < m and 0 <= (nc := c + dc) < n
            ]
        
        for i, j in product(range(m), range(n)):
            alive = board[i][j] >= 1
            live_neighbours_count = sum(board[ni][nj] >= 1 for ni, nj in get_neighbours(i, j))
            next_alive = will_be_alive(alive, live_neighbours_count)
            if alive and not next_alive: board[i][j] =  2
            if not alive and next_alive: board[i][j] = -1
        
        for i, j in product(range(m), range(n)):
            if board[i][j] ==  2: board[i][j] = 0
            if board[i][j] == -1: board[i][j] = 1
        
