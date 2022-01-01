class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix_sums = deque([[0] * len(matrix[0])])
        for row in matrix:
            next_row = list(map(operator.add, prefix_sums[-1], accumulate(row, operator.add)))
            prefix_sums.append(next_row)
        
        prefix_sums.popleft()
        self.prefix_sums = prefix_sums
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            (self.prefix_sums[row2][col2]) -
            (self.prefix_sums[row2][col1 - 1] if col1 > 0 else 0) -
            (self.prefix_sums[row1 - 1][col2] if row1 > 0 else 0) +
            (self.prefix_sums[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0)
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
