class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = list(Counter(arr).values())
        
        heapify(counts)
        while k and counts[0] <= k:
            k -= heappop(counts)
        
        return len(counts)
