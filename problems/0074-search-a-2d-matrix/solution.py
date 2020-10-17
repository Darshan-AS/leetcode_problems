class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = self.find_row(matrix, target)
        if row_index == -1: return False
        column_index = self.find_in_row(matrix[row_index], target)
        return column_index != -1
    
    def find_row(self, matrix: List[List[int]], target: int) -> int:
        low, high = 0, len(matrix) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            if not matrix[mid]: return -1
            val = matrix[mid][0]
            
            if target < val:
                high = mid - 1
            elif target > val:
                low = mid + 1
            else:
                return mid
        
        return low if low < len(matrix) and target > matrix[low][0] else high
            
    def find_in_row(self, arr: List[int], target: int) -> int:
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            val = arr[mid]
            
            if target < val:
                high = mid - 1
            elif target > val:
                low = mid + 1
            else:
                return mid
        
        return -1
