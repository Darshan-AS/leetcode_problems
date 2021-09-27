class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def min_path(r: int=0, i: int=0) -> int:
            if r >= len(triangle): return 0
            return min(min_path(r + 1, i), min_path(r + 1, i + 1)) + triangle[r][i]
        
        return min_path()
