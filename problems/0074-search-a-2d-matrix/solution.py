class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m_, n = len(matrix), len(matrix[0])
        l, r = 0, m_ * n - 1

        while l <= r:
            m = (l + r) // 2
            val = matrix[m // n][m % n]

            if   target < val: r = m - 1
            elif target > val: l = m + 1
            else: return True
        
        return False
