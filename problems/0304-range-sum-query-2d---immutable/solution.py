class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix_sums = [[0] * (len(matrix[0]) + 1)]
        for row in matrix:
            next_row = list(map(
                operator.add, 
                prefix_sums[-1], 
                accumulate(row, operator.add, initial=0),
            ))
            prefix_sums.append(next_row)
        
        self.prefix_sums = prefix_sums
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix_sums[row2 + 1][col2 + 1] -
            self.prefix_sums[row2 + 1][col1] -
            self.prefix_sums[row1][col2 + 1] +
            self.prefix_sums[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
