class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        n = len(dist)
        time = list(map(truediv, dist, speed))
        heapify(time)
        killed = takewhile(truth, (heappop(time) > t for t in range(n)))
        return sum(killed)
