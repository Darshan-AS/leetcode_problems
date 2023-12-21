class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        return max(starmap(sub, pairwise(sorted(map(itemgetter(0), points), reverse=True))))
        
