class Solution:
    def kClosest(self, points: list[list[int]], k_: int) -> list[list[int]]:
        
        def quick_select_first_k(
            seq: Sequence[Any],
            k: int,
            key: Callable[[Any], Any] = None,
            reverse: bool = False,
        ) -> Sequence[Any]:
            
            key = key if key else lambda x: x
            seq = list(seq)
            
            def partition(low: int, high: int) -> int:
                pivot_index, pivot = low, seq[low]
                
                while low <= high:
                    if (key(seq[low]) < key(pivot) if reverse else key(seq[low]) > key(pivot)):
                        seq[low], seq[high] = seq[high], seq[low]
                        high -= 1
                    else:
                        low += 1
                
                seq[pivot_index], seq[high] = seq[high], seq[pivot_index]
                return high
            
            i, j = 0, len(seq) - 1
            x, k = -1, k - 1
            while (x := partition(i, j)) != k:
                if x < k: i = x + 1
                elif x > k: j = x - 1
            
            return seq[: k + 1]
        
        squared_dist = lambda p1, p2: (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        squared_dist_from_origin = cache(partial(squared_dist, (0, 0)))
        
        return quick_select_first_k(list(map(tuple, points)), k_, key=squared_dist_from_origin)
