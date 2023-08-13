class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        partable = deque([True, False, nums[0] == nums[1]], 3)
        for i in range(2, n):
            partable.append(
                (nums[i] == nums[i - 1] and partable[-2]) or
                (nums[i] == nums[i - 1] == nums[i - 2] and partable[-3]) or
                (nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2 and partable[-3])
            )
        return partable[-1]

