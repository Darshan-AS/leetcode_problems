class Solution:
    def maxLength(self, arr: list[str]) -> int:
        def to_mask(s: str) -> int:
            return reduce(operator.or_, (1 << ord(ch) - ord('a') for ch in s))
        
        def bin_ones(n: int) -> int:
            return bin(n).count("1")
        
        @cache
        def max_concat(i: int, seen: int=0):
            if i == len(arr): return bin_ones(seen)
            x = to_mask(arr[i])
            return max(
                max_concat(i + 1, seen | x) if seen & x == 0 and bin_ones(x) == len(arr[i]) else 0,
                max_concat(i + 1, seen),
            )

        return max_concat(0)
