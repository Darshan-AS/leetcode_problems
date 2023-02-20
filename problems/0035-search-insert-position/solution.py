class Solution:
    def searchInsert(self, nums: list[int], k: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            l, r = (m + 1, r) if nums[m] < k else (l, m)
        return r
