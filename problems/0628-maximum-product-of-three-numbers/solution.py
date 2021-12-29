class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l1, l2, l3 = heapq.nlargest(3, nums)
        s1, s2 = heapq.nsmallest(2, nums)
        
        return max(l1 * l2 * l3, l1 * s1 * s2)
