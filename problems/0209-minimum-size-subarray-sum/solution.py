class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i, j, sum_, mlen = 0, 0, 0, inf
        while j < len(nums):
            sum_ += nums[j]; j += 1
            while sum_ >= target: mlen = min(mlen, j - i); sum_ -= nums[i]; i += 1;
        return 0 if mlen == inf else mlen
