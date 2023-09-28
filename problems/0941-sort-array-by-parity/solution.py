class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return sum(reduce(lambda a, x: a[x % 2].append(x) or a, nums, ([], [])), [])
        
