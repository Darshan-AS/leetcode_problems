class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j]:
                    g[i][j] = 0
                    continue
                elif i == 0 and j == 0:
                    g[i][j] = 1
                    continue
                
                if i > 0:
                    g[i][j] += g[i - 1][j]
                    
                if j > 0:
                    g[i][j] += g[i][j - 1]
        
        return g[-1][-1]
