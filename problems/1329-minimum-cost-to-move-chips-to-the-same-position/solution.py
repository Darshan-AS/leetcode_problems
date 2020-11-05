class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(s := sum(map(lambda x: x % 2, position)), len(position) - s)
