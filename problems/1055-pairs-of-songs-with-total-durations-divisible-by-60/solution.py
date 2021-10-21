class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        seen = collections.defaultdict(int)
        count = 0
        for t in map(lambda t: t % 60, time):
            count += seen[(60 - t) % 60]
            seen[t] += 1
        return count
