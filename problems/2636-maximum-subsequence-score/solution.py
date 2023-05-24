class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        nums = sorted(zip(nums2, nums1), reverse=True)
        hq = [nums[i][1] for i in range(k)]
        heapify(hq)

        sum_ = sum(hq)
        score = sum_ * nums[k - 1][0]
        for i in range(k, len(nums)):
            n2, n1 = nums[i]
            sum_ += n1 - heapreplace(hq, n1)
            score = max(score, sum_ * n2)
        return score

