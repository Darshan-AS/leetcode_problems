class Solution:
    def canCross(self, stones: list[int]) -> bool:
        stones_set = set(stones)

        @cache
        def can_jump(i: int, k: int) -> bool:
            return i == stones[-1] or any(
                x and x + i in stones_set and can_jump(i + x, x)
                for x in range(k - 1, k + 2)
            )
        
        return can_jump(stones[0], 0)
