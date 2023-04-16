class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        columns = list(map(Counter, zip(*words)))

        @cache
        def ways(i: int, j: int) -> int:
            if j < 0: return 1
            if i < 0: return 0
            col, ch = columns[i], target[j]
            return (ways(i - 1, j) + (ways(i - 1, j - 1) * col[ch] if ch in col else 0)) % 1_000_000_007
        
        return ways(len(columns) - 1, len(target) - 1)
