from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        location_count = defaultdict(int)
        for n, start, end in trips:
            location_count[start] += n
            location_count[end] -= n
        
        filled = 0
        for loc in sorted(location_count):
            filled += location_count[loc]
            if filled > capacity: return False
        return True
