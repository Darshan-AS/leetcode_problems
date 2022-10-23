class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # m: missing, d: duplicate
        n = len(nums)
        
        sum_all = n * (n + 1) // 2
        sq_sum_all = n * (n + 1) * (2 * n + 1) // 6
        
        diff = sum(nums) - sum_all # d - m
        sq_diff = sum(map(lambda x: x * x, nums)) - sq_sum_all # d^2 - m^2
        sum_ = sq_diff // diff # d + m
        
        return [(sum_ + diff) // 2, (sum_ - diff) // 2] # [d, m]
