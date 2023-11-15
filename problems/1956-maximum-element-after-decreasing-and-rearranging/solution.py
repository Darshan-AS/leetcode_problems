class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        n = len(arr)
        counts = Counter(map(min, arr, repeat(n)))
        return reduce(lambda a, x: min(a + counts.get(x, 0), x), range(1, n + 1))
        
