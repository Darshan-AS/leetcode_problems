from itertools import accumulate
from bisect import bisect
from random import randint, random

class Solution:

    def __init__(self, rects: List[List[int]]):
        def count_points_in(coordinates):
            x1, y1, x2, y2 = coordinates
            return (x2 - x1+ 1) * (y2 - y1 + 1)
        
        self.rects = rects
        weights = [(x2 - x1+ 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
        total = sum(weights)
        self.cummulative_probability = [i / total for i in accumulate(weights)]

    def pick(self) -> List[int]:
        index = bisect(self.cummulative_probability, random())
        x1, y1, x2, y2 = self.rects[index]
        return [randint(x1, x2), randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
