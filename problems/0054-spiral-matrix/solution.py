class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral_helper(i1, j1, i2, j2):
            if i1 > i2 or j1 > j2: return
            yield from (matrix[i1][j] for j in range(j1, j2 + 1))
            yield from (matrix[i][j2] for i in range(i1 + 1, i2 + 1))
            yield from (matrix[i2][j] for j in range(j2 - 1, j1 - 1, -1)) if i1 != i2 else tuple() 
            yield from (matrix[i][j1] for i in range(i2 - 1, i1, -1)) if j1 != j2 else tuple()
            yield from spiral_helper(i1 + 1, j1 + 1, i2 - 1, j2 - 1)
        
        return list(spiral_helper(0, 0, len(matrix) - 1, len(matrix[0]) - 1))
