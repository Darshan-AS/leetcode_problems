class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        T = TypeVar('T')
        def bisect(xs: Sequence[T], x: T, reverse: bool=False) -> int:
            l, r = 0, len(xs)

            while l < r:
                m = (l + r) // 2
                if x < xs[m]: r = m
                elif x > xs[m]: l = m + 1
                else: l, r = (m + 1, r) if reverse else (l, m)
            
            return l
        
        start, end = bisect(nums, target), bisect(nums, target, reverse=True) - 1
        return [start, end] if start <= end else [-1, -1]

