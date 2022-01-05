from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s_nums = SortedList()
        counts = []
        
        for num in reversed(nums):
            index = s_nums.bisect_left(num)
            counts.append(index)
            s_nums.add(num)
        
        return reversed(counts)
