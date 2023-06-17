class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2 = sorted(arr2)

        @cache
        def min_swaps(i: int, prev: int) -> int:
            if i >= len(arr1): return 0
            j = bisect.bisect(arr2, prev)
            keep = min_swaps(i + 1, arr1[i]) if arr1[i] > prev else inf
            swap = min_swaps(i + 1, arr2[j]) if j < len(arr2) else inf
            return min(keep, swap + 1)
        
        swaps = min_swaps(0, -1)
        return -1 if swaps is inf else swaps
        
