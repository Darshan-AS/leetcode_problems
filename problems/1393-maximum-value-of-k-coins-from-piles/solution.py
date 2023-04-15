class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k_: int) -> int:
        prefix_piles = [list(accumulate(p, initial=0)) for p in piles]

        @cache
        def max_value(n: int, k: int) -> int:
            return max(
                max_value(n - 1, k - i) + x
                for i, x in enumerate(islice(prefix_piles[n - 1], k + 1))
            ) if n and k else 0
        
        return max_value(len(piles), k_)
