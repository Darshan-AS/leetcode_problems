class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def abs_sort(sorted_nums: List[int]) -> List[int]:   
            origin = bisect.bisect_left(sorted_nums, 0)
            i, j = origin - 1, origin
        
            while i >= 0 and j < len(sorted_nums):
                yield sorted_nums[i] if -sorted_nums[i] < sorted_nums[j] else sorted_nums[j]
                i, j = (i - 1, j) if -sorted_nums[i] < sorted_nums[j] else (i, j + 1)

            yield from reversed(sorted_nums[:max(i + 1, 0)])
            yield from sorted_nums[j:]
        
        return list(map(lambda x: x * x, abs_sort(nums)))
