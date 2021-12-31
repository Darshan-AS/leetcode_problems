class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        prefix_maxs = list(accumulate(nums, max))
        suffix_mins = list(reversed(list(accumulate(reversed(nums), min))))
        
        def beauty(i: int) -> int:
            if not (1 <= i <= len(nums) - 2): return 0
            if prefix_maxs[i - 1] < nums[i] < suffix_mins[i + 1]: return 2
            elif nums[i - 1] < nums[i] < nums[i + 1]: return 1
            else: return 0

        return sum(map(beauty, range(len(nums))))
