class Solution:
    def numRollsToTarget(self, n_: int, k: int, target: int) -> int:
        @cache
        def num_rolls(n: int, t: int) -> int:
            return sum(
                num_rolls(n - 1, t - i)
                for i in range(1, k + 1)
                if i <= t
            ) % 1_000_000_007 if n and t else int(n == t)
        
        return num_rolls(n_, target)
