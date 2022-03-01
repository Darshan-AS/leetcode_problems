class Solution:
    def countBits(self, n: int) -> list[int]:
        return list(map(Solution.count_bit, range(n + 1)))
    
    @cache
    @staticmethod
    def count_bit(n: int) -> int:
        return Solution.count_bit(n // 2) + (n % 2) if n else 0
