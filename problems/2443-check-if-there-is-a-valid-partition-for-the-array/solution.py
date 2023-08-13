class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        return reduce(
            lambda p, i: p.append(
                (nums[i] == nums[i - 1] and p[-2]) or
                (nums[i] == nums[i - 1] == nums[i - 2] and p[-3]) or
                (nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2 and p[-3])
            ) or p,
            range(2, len(nums)),
            deque([True, False, nums[0] == nums[1]], 3),
        )[-1]

