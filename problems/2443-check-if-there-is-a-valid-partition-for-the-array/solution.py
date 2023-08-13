class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        @cache
        def partable(i: int) -> bool:
            return (
                (i < 0) or
                (i > 0 and nums[i] == nums[i - 1] and partable(i - 2)) or
                (i > 1 and nums[i] == nums[i - 1] == nums[i - 2] and partable(i - 3)) or
                (i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2 and partable(i - 3))
            )
        
        return partable(len(nums) - 1)

