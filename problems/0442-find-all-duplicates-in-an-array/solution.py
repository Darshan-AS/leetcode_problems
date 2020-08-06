class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                dups.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return dups
