class Solution:
    def stoneGameIII(self, values: list[int]) -> str:
        @cache
        def score(i: int) -> int:
            return (i < len(values)) and max(sum(values[i : j]) - score(j) for j in range(i + 1, i + 4))
        
        s = score(0)
        return 'Tie' if s == 0 else ('Alice' if s > 0 else 'Bob')
