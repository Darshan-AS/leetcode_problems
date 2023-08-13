class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        partable = [False] * (n + 1)
        partable[0] = True

        for i in range(n):
            k = i + 1
            partable[k] = (
                (i > 0 and nums[i] == nums[i - 1] and partable[k - 2]) or
                (i > 1 and nums[i] == nums[i - 1] == nums[i - 2] and partable[k - 3]) or
                (i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2 and partable[k - 3])
            )
        
        return partable[-1]

