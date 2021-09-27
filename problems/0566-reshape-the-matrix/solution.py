from itertools import chain

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        flat_mat = chain.from_iterable(mat)
        return [[next(flat_mat) for _ in range(c)] for _ in range(r)] if r * c == m * n else mat
