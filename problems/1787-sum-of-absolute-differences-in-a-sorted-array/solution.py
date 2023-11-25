class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        return [
            i * x - p + (s - p) - (len(nums) - i) * x
            for i, x, p, s in zip(
                count(1),           # index
                nums,               # num
                accumulate(nums),   # prefix sums
                repeat(sum(nums),   # sum of nums
            ))
        ]
        
