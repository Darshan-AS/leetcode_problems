class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        xs = sorted(arr)
        M = 1_000_000_007

        counts = dict(zip(xs, repeat(1)))
        for x in xs:
            counts[x] += sum(
                (counts[y] * counts[x // y]) % M
                for y in takewhile(lambda y: y < x, xs)
                if x % y == 0 and x // y in counts
            ) % M
        
        return sum(counts.values()) % M
