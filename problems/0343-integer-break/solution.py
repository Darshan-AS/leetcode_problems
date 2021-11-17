class Solution:
    def integerBreak(self, num: int) -> int:
        @cache
        def int_break(n: int) -> int:
            return max(int_break(n - 3) * 3, int_break(n - 2) * 2) if n >= 4 else n
        
        return int_break(num) + (0 if num >= 4 else -1)
