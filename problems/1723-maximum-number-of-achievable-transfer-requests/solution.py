class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        k = len(requests)
        masks = (map(int, bin(i)[2:].zfill(k)) for i in range(1, 2 ** k))
        powerset_reqs = (compress(requests, m) for m in masks)
        def handle_req(counts, u, v): counts[u] -= 1; counts[v] += 1; return 1
        count_diffs = ((sum(handle_req(counts, u, v) for u, v in p), any(counts.values())) for p in powerset_reqs for counts in (defaultdict(int),))
        return max(filterfalse(itemgetter(1), count_diffs), default=(0, False))[0]
