import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extra_students: int) -> float:
        delta_pass = lambda passed, total: (passed + 1)/(total + 1) - passed/total
        
        hq = [(-delta_pass(p, t), p, t) for p, t in classes]
        heapq.heapify(hq)
        
        for _ in range(extra_students):
            _, p, t = heapq.heappop(hq)
            heapq.heappush(hq, (-delta_pass(p + 1, t + 1), p + 1, t + 1))
        
        return sum(p/t for _, p, t in hq) / len(classes)
