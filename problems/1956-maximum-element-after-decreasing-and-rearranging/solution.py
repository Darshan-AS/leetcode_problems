class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        return reduce(lambda a, x: a + (x > a), sorted(arr), 0)
        
