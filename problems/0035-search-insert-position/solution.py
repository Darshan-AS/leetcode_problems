class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, value in enumerate(nums):
            if value >= target:
                return i
        return len(nums)
