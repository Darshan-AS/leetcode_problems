class Solution:
    def stoneGameIII(self, stone_value: list[int]) -> str:
        n = len(stone_value)
        suffix_sums = tuple(reversed(tuple(accumulate(reversed(stone_value)))))

        @cache
        def score(i: int) -> int:
            return max(suffix_sums[i] - score(i + x) for x in range(1, 4)) if i < n else 0
        
        s = suffix_sums[0]
        a = score(0)
        b = s - a
        return 'Tie' if a == b else ('Alice' if a > b else 'Bob')
