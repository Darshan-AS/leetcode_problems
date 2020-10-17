class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            val = matrix[mid // n][mid % n]
            
            if target < val:
                high = mid - 1
            elif target > val:
                low = mid + 1
            else:
                return True
        
        return False
