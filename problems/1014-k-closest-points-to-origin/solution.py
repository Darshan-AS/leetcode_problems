class Solution:
    def kClosest(self, points: List[List[int]], k_: int) -> List[List[int]]:
        def quick_select_first_k(seq: Sequence, k: int) -> Sequence:
            def partition(low: int, high: int) -> int:
                pivot_index, pivot = low, seq[low]
                
                while low <= high:
                    if seq[low] > pivot:
                        seq[low], seq[high] = seq[high], seq[low]
                        high -= 1
                    else:
                        low += 1
                
                seq[high], seq[pivot_index] = seq[pivot_index], seq[high]
                return low
            
            n = len(seq)
            i, j = 0, n - 1
            x = 0
            while x != k:
                x = partition(i, j)
                if x < k: i = x
                elif x > k: j = x - 1
            
            return seq[:k]
        
        
        
        
        squared_dist = lambda p1, p2: (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        squared_dist_from_origin = functools.partial(squared_dist, (0, 0))
        
        dists = [(squared_dist_from_origin(p), p) for p in points]
        return [p for _, p in quick_select_first_k(dists, k_)]
