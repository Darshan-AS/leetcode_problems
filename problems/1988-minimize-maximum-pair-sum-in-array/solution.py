class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        return max(map(add, (xs := sorted(nums)), reversed(xs)))
        
