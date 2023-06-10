class Solution:
    def maxValue(self, n: int, index: int, max_sum: int) -> int:
        sum_ = lambda k: k * (k + 1) // 2 if k >= 0 else k
        l, r = 1, max_sum
        while l <= r:
            m = (l + r) // 2
            curr_sum = sum_(m) - sum_(m - index - 1) + sum_(m) - sum_(m - n + index) - m
            l, r = (m + 1, r) if curr_sum <= max_sum else (l, m - 1)
        return r
