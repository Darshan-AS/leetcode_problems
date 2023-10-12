class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        starts, ends = map(sorted, zip(*flowers))
        return [bisect_right(starts, p) - bisect_right(ends, p - 1) for p in people]
