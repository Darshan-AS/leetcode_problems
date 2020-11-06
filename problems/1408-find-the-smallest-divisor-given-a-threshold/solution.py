from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = max(sum(nums) // threshold, 1)
        right = sum(nums) // max(threshold - len(nums), 1)
        
        while left <= right:
            mid = left + (right - left) // 2
            val = sum(map(lambda i: ceil(i / mid), nums))
            if val <= threshold:
                right = mid - 1
            elif val > threshold:
                left = mid + 1
        return left
