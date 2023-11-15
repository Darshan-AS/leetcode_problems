class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        return (c := Counter(map(min, arr, repeat(len(arr))))) and reduce(lambda a, x: min(a + c.get(x, 0), x), range(1, len(arr) + 1))
        
