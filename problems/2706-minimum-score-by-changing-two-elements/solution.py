class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        k, n = 2, len(nums)
        min_hq, max_hq = list(nums), list(map(neg, nums))
        heapify(min_hq); heapify(max_hq)

        maxs = tuple(-heappop(max_hq) for _ in range(min(k + 1, n)))
        mins = tuple( heappop(min_hq) for _ in range(min(k + 1, n)))

        return min(map(sub, maxs, reversed(mins)))
