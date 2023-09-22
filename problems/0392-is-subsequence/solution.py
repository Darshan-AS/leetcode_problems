class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        get_or = lambda xs, i, default: xs[i] if i < len(xs) else default
        idxs = reduce(lambda a, x: a[x[1]].append(x[0]) or a, enumerate(t), defaultdict(list))
        picked_idxs = accumulate(s, lambda a, x: get_or(idxs[x], bisect_left(idxs[x], a), inf) + 1, initial=0)
        return inf not in picked_idxs

