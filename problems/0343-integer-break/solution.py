class Solution:
    def integerBreak(self, num: int) -> int:
        @cache
        def int_break(n: int) -> int:
            return max(*(int_break(n - i) * i for i in range(1, n)), n) if n > 1 else 1
        
        return int_break(num) if num >= 4 else num - 1
