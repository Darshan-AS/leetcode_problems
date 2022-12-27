class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], k: int) -> int:
        remaining = map(sub, capacity, rocks)
        prefix_sums = accumulate(sorted(remaining))
        full_bags = takewhile(lambda x: x <= k, prefix_sums)
        return sum(1 for _ in full_bags)
