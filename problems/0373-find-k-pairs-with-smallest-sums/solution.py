class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        n1, n2 = len(nums1), len(nums2)
        sumsq = [(nums1[i] + nums2[0], i, 0) for i in range(n1)]
        heapify(sumsq)
        
        smallest = []
        for _ in range(min(k, n1 * n2)):
            sum_, i, j = heappop(sumsq)
            smallest.append([nums1[i], nums2[j]])
            if j + 1 < n2: heappush(sumsq, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return smallest
