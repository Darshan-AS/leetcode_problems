class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        return reduce(
            lambda a, x: (a[0] + 1, x[1]) if x[0] > a[1] else a,
            sorted(pairs, key=itemgetter(1)),
            (0, -inf), # (chain_len, previous_right)
        )[0]
