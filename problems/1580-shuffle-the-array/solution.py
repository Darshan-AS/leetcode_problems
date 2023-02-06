class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return [nums[j] for i in range(n) for j in (i, i + n)]
