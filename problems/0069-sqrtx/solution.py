class Solution:
    def mySqrt(self, x: int) -> int:
        a = x
        while a * a > x:
            a = int((a + x / a) / 2)
        return a
