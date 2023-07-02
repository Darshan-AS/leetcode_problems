class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        is_achievable = lambda reqs: not any((Counter(u for u, _ in reqs) - Counter(v for _, v in reqs)).values())
        powerset_reqs = chain.from_iterable(combinations(requests, k) for k in range(len(requests), 0, -1))
        return next(map(len, filter(is_achievable, powerset_reqs)), 0)
