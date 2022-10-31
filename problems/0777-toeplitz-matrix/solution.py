class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        tail = lambda xs: islice(xs, 1, None)
        iter_eq = lambda xs, ys: all(map(eq, xs, ys))
        
        return all(starmap(lambda r1, r2: iter_eq(r1, tail(r2)), pairwise(matrix)))

