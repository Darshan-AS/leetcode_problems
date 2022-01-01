class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        get_at = lambda matrix, r, c, default=0: matrix[r][c] if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) else default
        
        prefix_sum = [[0] * n for _ in range(m)]
        for i, j in product(range(m), range(n)):
            prefix_sum[i][j] = (
                get_at(prefix_sum, i, j - 1) +
                get_at(prefix_sum, i - 1, j) -
                get_at(prefix_sum, i - 1, j - 1) +
                get_at(mat, i, j)
            )
            
        k_sum = [[0] * n for _ in range(m)]
        for i, j in product(range(m), range(n)):
            k_sum[i][j] = (
                get_at(prefix_sum, min(i + k, m - 1), min(j + k, n - 1)) -
                get_at(prefix_sum, min(i + k, m - 1), j - k - 1) -
                get_at(prefix_sum, i - k - 1, min(j + k, n - 1)) +
                get_at(prefix_sum, i - k - 1, j - k - 1)
            )
        
        return k_sum
