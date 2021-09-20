class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        players = ('A', 'B')
        board = [[''] * n for _ in range(n)]
        
        # Construct the end state of the board
        for move, player in zip(moves, itertools.cycle(players)):
            board[move[0]][move[1]] = player
        
        rows = (((i, j) for j in range(n)) for i in range(n))
        cols = (((i, j) for i in range(n)) for j in range(n))
        digs = (((i, i) for i in range(n)), ((i, n - i -1) for i in range(n)))
        
        # Check for each row, column, and diagonal
        for vector in chain(rows, cols, digs):
            # If all values are same and is a player symbol then the player won
            choice_set = {board[i][j] for i, j in vector}
            if len(choice_set) == 1 and (player := choice_set.pop()) in players:
                return player
        
        # Draw if all moves have been made else Pending
        return 'Draw' if len(moves) == n * n else 'Pending'
