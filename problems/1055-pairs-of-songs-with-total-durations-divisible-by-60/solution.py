class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        seen = collections.defaultdict(int)
        count = 0
        for t in map(lambda t: t % 60, time):
            if t == 0:
                count += seen[0]
            elif 60 - t in seen:
                count += seen[60 - t]
            seen[t] += 1
        return count
