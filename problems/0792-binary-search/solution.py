class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = ceil((l + r) / 2)
            l, r = (l, m - 1) if target < nums[m] else (m, r)
        return l if nums[l] == target else -1
