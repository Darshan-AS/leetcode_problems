class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        return sum(itemgetter(*zip(*grid), 0)(Counter(map(tuple, grid))))
