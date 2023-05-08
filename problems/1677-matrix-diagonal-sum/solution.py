class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        return (n := len(mat)) and sum(
            mat[i][i] + mat[i][n - 1 - i] for i in range(n)
        ) - mat[n // 2][n // 2] * (n % 2)

