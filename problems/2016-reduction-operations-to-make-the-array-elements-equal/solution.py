class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        return sum(i * v for i, (k, v) in enumerate(sorted(Counter(nums).items())))
        
