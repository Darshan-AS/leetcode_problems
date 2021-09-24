class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist_mat = [[float("inf")] * n for _ in range(m)]

        get_at = lambda x, y: dist_mat[x][y] if 0 <= x < m and 0 <= y < n else float("inf")
        
        # top-left to bottom-right
        for i, j in itertools.product(range(m), range(n)):
            dist_mat[i][j] = (
                0
                if mat[i][j] == 0
                else min(dist_mat[i][j], min(get_at(i - 1, j), get_at(i, j - 1)) + 1)
            )
        
        # bottom-right to top-left
        for i, j in itertools.product(range(m - 1, -1, -1), range(n - 1, -1, -1)):
            dist_mat[i][j] = (
                0
                if mat[i][j] == 0
                else min(dist_mat[i][j], min(get_at(i + 1, j), get_at(i, j + 1)) + 1)
            )

        return dist_mat

