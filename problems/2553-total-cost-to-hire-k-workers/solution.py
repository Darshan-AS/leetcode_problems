class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        l, r = candidates, n - candidates - 1

        l_bucket = zip(range(l), repeat(0))
        r_bucket = zip(range(max(l, r + 1), n), repeat(1))

        hq = [(costs[idx], bucket) for idx, bucket in chain(l_bucket, r_bucket)]
        heapq.heapify(hq)

        cost = 0
        for _ in range(k):
            c, b = heapq.heappop(hq)
            cost += c

            if l > r: continue

            idx = (l, r)[b]
            l, r = (l, r - 1) if b else (l + 1, r)
            heapq.heappush(hq, (costs[idx], b))
        
        return cost
