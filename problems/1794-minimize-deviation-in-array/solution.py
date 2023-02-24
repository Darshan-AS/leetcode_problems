from sortedcontainers import SortedList

class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        sl = SortedList(n * 2 if n % 2 else n for n in nums)

        min_deviation = sl[-1] - sl[0]
        while sl[-1] % 2 == 0:
            sl.add(sl.pop() // 2)
            min_deviation = min(min_deviation, sl[-1] - sl[0])
        return min_deviation
