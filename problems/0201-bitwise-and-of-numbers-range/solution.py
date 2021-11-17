class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        return n & m & (-1 << ceil(log(n - m, 2))) if m and m != n else m
