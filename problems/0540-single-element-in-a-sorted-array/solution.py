class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            i, j = (m - 1, m) if m % 2 else (m, m + 1)
            l, r = (j + 1, r) if nums[i] == nums[j] else (l, i)
        return nums[r]
