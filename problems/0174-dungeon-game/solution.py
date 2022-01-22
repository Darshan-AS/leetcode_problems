class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        @cache
        def min_hp(i: int, j: int) -> int:
            if not (0 <= i < m and 0 <= j < n): return math.inf
            x = dungeon[i][j]
            
            if (i, j) == (m - 1, n - 1):
                return 1 if x > 0 else -(x - 1)
            
            hp = min(min_hp(i + 1, j), min_hp(i, j + 1))
            return max(hp - x, 1)

        
        return min_hp(0, 0)
            
