from math import sqrt
from itertools import combinations
from collections import Counter

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dist = lambda pa, pb: sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
        
        c = Counter(map(lambda x: dist(*x), combinations([p1, p2, p3, p4], 2)))
        return list(sorted(c.values())) == [2, 4]
