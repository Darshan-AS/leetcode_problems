class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        
        seen = set()
        def is_sub_island(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in seen or not grid2[i][j]: return True
            
            seen.add((i, j))
            sub_island = bool(grid1[i][j])
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                sub_island = is_sub_island(i + di, j + dj) and sub_island
            return sub_island
        
        return sum(
            grid2[i][j] and 
            (i, j) not in seen and 
            is_sub_island(i, j) 
            for i, j in product(range(m), range(n))
        )
            
