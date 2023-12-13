class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_sums = list(map(sum, mat))
        col_sums = list(map(sum, zip(*mat)))
        return sum(1 == mat[i][j] == row_sums[i] == col_sums[j] for i, j in product(range(m), range(n)))
        
