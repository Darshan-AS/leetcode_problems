class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = [0] * n
        
        for i in range(m):
            for j in range(n):
                min_val = 0
                if j == 0: min_val = cache[j]
                elif i == 0: min_val = cache[j - 1]
                else: min_val = min(cache[j - 1], cache[j])
                    
                cache[j] = min_val + grid[i][j]
                
        return cache[-1]
