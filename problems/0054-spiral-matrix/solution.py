class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    
        def inwards_spiral(m: int, n: int) -> Iterator[Tuple[int, int]]:
            
            for k in range((min(m, n) + 1) // 2):
                (i1, j1), (i2, j2) = (k, k), (m - k - 1, n - k - 1)
                
                if (i1, j1) == (i2, j2): yield (i1, j1); return
                
                yield from ((i1, j) for j in range(j1, j2))
                yield from ((i, j2) for i in range(i1, i2))
                yield from ((i2, j) for j in range(j2, j1, -1)) if i1 != i2 else ((i2, j2),)
                yield from ((i, j1) for i in range(i2, i1, -1)) if j1 != j2 else ((i2, j1),)
        
        
        return [matrix[i][j] for i, j in inwards_spiral(len(matrix), len(matrix[0]))]
