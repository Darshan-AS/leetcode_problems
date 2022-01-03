class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        
        def clash(p1: tuple[int, int], p2: tuple[int, int]) -> bool:
            r1, c1 = p1
            r2, c2 = p2
            return r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2)
        
        def n_queens(col: int, placed: list):
            if col == n:
                solutions.append(placed.copy())
            
            for row in range(n):
                if any(clash(p, (row, col)) for p in placed):
                    continue
                
                placed.append((row, col))
                n_queens(col + 1, placed)
                placed.pop()
        
        n_queens(0, [])
        
        board = lambda size: [['.'] * size for _ in range(size)]
        
        boards = []
        for solution in solutions:
            b = board(n)
            for r, c in solution:
                b[r][c] = 'Q'
            boards.append(b)
        
        return [list(map(''.join, b)) for b in boards]
