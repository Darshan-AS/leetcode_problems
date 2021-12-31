class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        prefix_mins = accumulate(nums, min, initial=math.inf)
        max_diff = max(map(operator.sub, nums, prefix_mins))
        return max_diff if max_diff > 0 else -1
