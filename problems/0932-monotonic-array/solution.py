class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return all(starmap(ge, pairwise(nums))) or all(starmap(le, pairwise(nums)))
