class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        
        left = zip(range(m - 1), repeat(0))
        bottom = zip(repeat(m - 1), range(n))     
        
        top = zip(repeat(0), range(n - 1))
        right = zip(range(m), repeat(n - 1))
        
        up_starts = islice(chain(left, bottom), 0, None, 2)
        down_starts = islice(chain(top, right), 1, None, 2)
        
        all_starts = chain.from_iterable(zip_longest(up_starts, down_starts))
        starts_and_direction = zip(all_starts, cycle(((-1, 1), (1, -1))))
        
        advance = lambda prev, direction: (prev[0] + direction[0], prev[1] + direction[1])
        diagonal_from = lambda start, direction: accumulate(repeat(direction), advance, initial=start)
        
        inbounds = lambda x: 0 <= x[0] < m and 0 <= x[1] < n
        
        diagonal_indices = chain.from_iterable(starmap(
            lambda s, d: takewhile(inbounds, diagonal_from(s, d)),
            starts_and_direction,
        ))
        
        return [mat[i][j] for i, j in diagonal_indices]
        
