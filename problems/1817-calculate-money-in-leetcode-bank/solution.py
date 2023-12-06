class Solution:
    def totalMoney(self, n: int) -> int:
        q, r = divmod(n, 7)
        full = q * 28 + ((q - 1) * q // 2) * 7
        last = (r * (r + 1) // 2) + q * r
        return full + last
