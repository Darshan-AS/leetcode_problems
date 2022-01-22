class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0]) # Always a square matrix

        # (i, j) -> (j, n - i - 1) -> (n - i - 1, n - j - 1) -> (n - j - 1, i)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                (
                    matrix[i][j],
                    matrix[j][n - i - 1],
                    matrix[n - i - 1][n - j - 1],
                    matrix[n - j - 1][i],
                ) = (
                    matrix[n - j - 1][i],
                    matrix[i][j],
                    matrix[j][n - i - 1],
                    matrix[n - i - 1][n - j - 1],
                )
