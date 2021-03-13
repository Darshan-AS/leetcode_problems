class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        val_at = lambda index: matrix[index // n][index - (index // n) * n]
        
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            val = val_at(mid)
            
            if target < val:
                right = mid - 1
            elif target > val:
                left = mid + 1
            else:
                return True
        
            
        return False
