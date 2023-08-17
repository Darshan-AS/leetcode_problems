class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        dists = [[inf] * n for _ in range(m)]

        get_at = lambda x, y: dists[x][y] if 0 <= x < m and 0 <= y < n else inf

        # top-left to bottom-right
        for i, j in product(range(m), range(n)):
            dists[i][j] = mat[i][j] and min(dists[i][j], min(get_at(i - 1, j), get_at(i, j - 1)) + 1)
        
        # bottom-right to top-left
        for i, j in product(range(m - 1, -1, -1), range(n - 1, -1, -1)):
            dists[i][j] = mat[i][j] and min(dists[i][j], min(get_at(i + 1, j), get_at(i, j + 1)) + 1)
        
        return dists
