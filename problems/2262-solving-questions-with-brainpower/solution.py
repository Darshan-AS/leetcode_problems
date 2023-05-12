class Solution:
    def mostPoints(self, qns: list[list[int]]) -> int:
        @cache
        def max_score(i: int) -> int:
            return i < len(qns) and max(qns[i][0] + max_score(i + 1 + qns[i][1]), max_score(i + 1))
        
        return max_score(0)
