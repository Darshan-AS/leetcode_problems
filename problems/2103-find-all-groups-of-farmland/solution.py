class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        seen = set()
        def find_farmland(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in seen or not land[i][j]:
                return (math.inf, math.inf), (-math.inf, -math.inf)
            
            top_left = bottom_right = (i, j)
            seen.add((i, j))
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                tl, br = find_farmland(i + di, j + dj)
                top_left = min(top_left, tl)
                bottom_right = max(bottom_right, br)
            return top_left, bottom_right
        
        m, n = len(land), len(land[0])
        return [list(chain(*find_farmland(i, j))) for i, j in product(range(m), range(n)) if land[i][j] and (i, j) not in seen]
