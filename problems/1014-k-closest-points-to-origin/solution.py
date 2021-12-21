class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_between = lambda p1, p2: math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        dist_from_origin = functools.partial(dist_between, (0, 0))
        
        dists = [(dist_from_origin(p), p) for p in points]
        heapq.heapify(dists)
        return [heapq.heappop(dists)[1] for _ in range(k)]
