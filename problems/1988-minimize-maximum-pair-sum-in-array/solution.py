class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        return max(islice(map(add, (xs := sorted(nums)), reversed(xs)), len(nums) // 2))
        
