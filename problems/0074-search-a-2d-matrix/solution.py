class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if target > matrix[-1][-1]: return False
        row = bisect_left(matrix, target, key=itemgetter(-1))
        col = bisect_left(matrix[row], target)
        return matrix[row][col] == target
