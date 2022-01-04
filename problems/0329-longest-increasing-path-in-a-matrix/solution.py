class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # Don't need classic DFS previously seen set as the sequence is increasing
        @cache
        def longest_increasing_path_from(i: int, j: int) -> int:            
            return max((
                longest_increasing_path_from(next_i, next_j)
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1))
                if (
                    0 <= (next_i := i + di) < m and
                    0 <= (next_j := j + dj) < n and
                    matrix[next_i][next_j] > matrix[i][j]
                )),
                default = 0,
            ) + 1
        
        return max(starmap(longest_increasing_path_from, product(range(m), range(n))))
