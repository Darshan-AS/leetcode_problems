class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        xs = [0] * 1001
        
        for np, fr, to in trips:
            xs[fr] -= np
            xs[to] += np
        
        return all(x >= 0 for x in accumulate(xs, operator.add, initial=capacity))
        
