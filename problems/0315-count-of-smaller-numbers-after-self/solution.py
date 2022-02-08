from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        sl = SortedList(nums)
        counts = [sl.remove(num) or sl.bisect_left(num) for num in nums]
        return counts
