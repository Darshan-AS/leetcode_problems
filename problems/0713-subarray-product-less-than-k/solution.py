class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        j = 0
        count = 0
        prod = 1
        for i in range(len(nums)):
            prod /= nums[i - 1] if i > 0 else 1
            while j < len(nums) and prod * nums[j] < k:
                prod *= nums[j]
                j += 1
            count += max(j - i, 0)
        return count
