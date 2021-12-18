class Solution:
    def integerBreak(self, num: int) -> int:
        @cache
        def int_break(n: int) -> int:
            return max(
                max(int_break(n - i), n - i) * i
                for i in range(1, n // 2 + 1)
            ) if n > 1 else 1
        
        return int_break(num)
