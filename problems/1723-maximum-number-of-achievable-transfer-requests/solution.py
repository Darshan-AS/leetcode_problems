class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        powerset_reqs = chain.from_iterable(combinations(requests, k) for k in range(len(requests), 0, -1))
        transposed_reqs = (zip(*p) for p in powerset_reqs)
        count_diffs = ((len(us), any((Counter(us) - Counter(vs)).values())) for us, vs in transposed_reqs)
        return next(filterfalse(itemgetter(1), count_diffs), (0, False))[0]
