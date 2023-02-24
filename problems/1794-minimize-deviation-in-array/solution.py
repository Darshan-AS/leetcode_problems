class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        hq = [-n * 2 if n % 2 else -n for n in nums]
        heapify(hq)

        min_ = -min(hq, key=neg)
        min_deviation = -hq[0] - min_

        while hq and hq[0] % 2 == 0:
            n = heappop(hq) // 2
            heappush(hq, n)
            min_ = min(min_, -n)
            min_deviation = min(min_deviation, - hq[0] - min_)
        
        return min_deviation

