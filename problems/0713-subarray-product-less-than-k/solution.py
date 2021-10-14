class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        i = j = 0
        product = 1
        while j < len(nums):
            product *= nums[j]
            while i <= j and product >= k:
                product //= nums[i]
                i += 1
            count += j - i + 1
            j += 1
        
        return count
