class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions_count = 0
        
        def clash(p1: tuple[int, int], p2: tuple[int, int]) -> bool:
            r1, c1 = p1
            r2, c2 = p2
            return r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2)
        
        def n_queens(col: int, placed: list):
            nonlocal solutions_count
            
            if col == n:
                solutions_count += 1
            
            for row in range(n):
                if any(clash(p, (row, col)) for p in placed):
                    continue
                
                placed.append((row, col))
                n_queens(col + 1, placed)
                placed.pop()
        
        n_queens(0, [])
        return solutions_count
