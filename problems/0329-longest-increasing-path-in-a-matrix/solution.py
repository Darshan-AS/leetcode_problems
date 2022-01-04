class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        seen = set()
        
        @cache
        def longest_increasing_path_from(i: int, j: int) -> int:
            seen.add((i, j))
            
            max_len = max((
                longest_increasing_path_from(next_i, next_j)
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1))
                if (
                    0 <= (next_i := i + di) < m and
                    0 <= (next_j := j + dj) < n and
                    (next_i, next_j) not in seen and
                    matrix[next_i][next_j] > matrix[i][j]
                )),
                default = 0,
            ) + 1
            
            seen.remove((i, j))
            
            return max_len
            
        
        return max(starmap(longest_increasing_path_from, product(range(m), range(n))))
