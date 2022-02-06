class Solution:
    def findKthLargest(self, nums: list[int], k_: int) -> int:
        
        def quick_select(
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
            
            return seq[k]
        
        return quick_select(nums, k_, reverse=True)
