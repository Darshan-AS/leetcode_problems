class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = j = 0
        length = n + 1
        curr_sum = 0
        while j < n:
            curr_sum += nums[j]
            while i <= j and curr_sum >= target:
                length = min(length, j - i + 1)
                curr_sum -= nums[i]
                i += 1
            j += 1
        return length if length <= n else 0
