class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        min1 = min2 = 0
        min1_index = 0
        
        for i in range(m):
            tmin1 = tmin2 = math.inf
            
            for j in range(n):
                curr_min = (min1 if min1_index != j else min2) + grid[i][j]
                
                if curr_min < tmin1:
                    tmin1, tmin2 = curr_min, tmin1
                    tmin1_index = j
                elif curr_min < tmin2:
                    tmin2 = curr_min
            
            min1, min2, min1_index = tmin1, tmin2, tmin1_index
        
        return min1
