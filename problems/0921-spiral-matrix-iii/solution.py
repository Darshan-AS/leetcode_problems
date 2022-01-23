class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r_start: int, c_start: int) -> List[List[int]]:
        
        def outwards_spiral(i_start: int, j_start: int) -> Iterator[Tuple[int, int]]:
            m, n = i_start, j_start
            
            for k in count(0):
                (i1, j1), (i2, j2) = (m - k, n - k), (m + k + 1, n + k + 1)
                                
                yield from ((i1, j) for j in range(j1, j2))
                yield from ((i, j2) for i in range(i1, i2))
                yield from ((i2, j) for j in range(j2, j1 - 1, -1))
                yield from ((i, j1 - 1) for i in range(i2, i1 - 1, -1))
        
        return list(islice(filter(
            lambda x: 0 <= x[0] < rows and 0 <= x[1] < cols,
            outwards_spiral(r_start, c_start),
        ), rows * cols))
