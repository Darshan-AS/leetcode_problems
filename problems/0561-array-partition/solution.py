class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(islice(sorted(nums), 0, None, 2))
