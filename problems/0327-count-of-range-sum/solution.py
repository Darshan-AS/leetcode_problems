from sortedcontainers import SortedList

class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        sl = SortedList([0])

        count = 0
        for s in accumulate(nums):
            i = sl.bisect_left(s - upper)
            j = sl.bisect_right(s - lower)
            count += j - i
            sl.add(s)

        return count
