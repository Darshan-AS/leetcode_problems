class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        def transpose(m: list[list]) -> list[list]:
            return list(map(list, zip(*m)))
        
        # Column wise cummulative count of 1s (Hint 1)
        m_ = [list(accumulate(xs, lambda a, x: a + x if x else x)) for xs in transpose(matrix)]
        # Row wise sort in decreasing order
        m  = [sorted(xs, reverse=True) for xs in transpose(m_)]
        # Index wise max matrix possible
        return max(i * x for r in m for i, x in enumerate(r, 1))
