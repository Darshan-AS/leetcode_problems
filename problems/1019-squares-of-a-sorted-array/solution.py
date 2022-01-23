class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def abs_sort(sorted_nums: List[int]) -> List[int]:   
            origin = bisect.bisect_left(sorted_nums, 0)
            i, j = origin - 1, origin
        
            while i >= 0 and j < len(sorted_nums):
                if abs(sorted_nums[i]) < abs(sorted_nums[j]):
                    yield sorted_nums[i]
                    i -= 1
                else:
                    yield sorted_nums[j]
                    j += 1

            yield from reversed(sorted_nums[:max(i + 1, 0)])
            yield from sorted_nums[j:]
        
        return list(map(lambda x: x * x, abs_sort(nums)))
