class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        T, V = TypeVar('T'), TypeVar('V')
        Key = Callable[[T], V]

        def quick_select(seq: Sequence[T], k: int, key: Key = None, reverse: bool = False) -> T:
            key = (lambda x: x) if key is None else key
            seq = list(seq)

            def partition(l: int, r: int) -> int:
                pivot_idx, pivot = l, seq[l]

                while l <= r:
                    swap = key(seq[l]) < key(pivot) if reverse else key(seq[l]) > key(pivot)
                    seq[l], seq[r] = (seq[r], seq[l]) if swap else (seq[l], seq[r])
                    l, r = (l, r - 1) if swap else (l + 1, r)
                
                seq[pivot_idx], seq[r] = seq[r], seq[pivot_idx]
                return r

            
            i, j = 0, len(seq) - 1
            k = k - 1
            while (x := partition(i, j)) != k:
                i, j = (x + 1, j) if x < k else (i, x - 1)
            
            return seq[k]
        
        
        return quick_select(nums, k, reverse=True)
