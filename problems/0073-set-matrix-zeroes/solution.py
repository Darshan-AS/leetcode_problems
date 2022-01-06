class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        
        first_row_has_0 = 0 in matrix[0]
        first_col_has_0 = 0 in next(zip(*matrix))
        
        for i, j in product(range(1, m), range(1, n)):
            if not matrix[i][j]:
                matrix[i][0] = matrix[0][j] = 0
        
        for i, j in product(range(1, m), range(1, n)):
            if not (matrix[i][0] and matrix[0][j]):
                matrix[i][j] = 0
        
        if first_row_has_0:
            for j in range(n): matrix[0][j] = 0   
                
        if first_col_has_0:
            for i in range(m): matrix[i][0] = 0

