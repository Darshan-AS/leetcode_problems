class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [set()]
        for num in nums:
            power_set.extend([p | {num} for p in power_set])
        return power_set
