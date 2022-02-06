class Solution:
    def findKthLargest(self, nums: list[int], k_: int) -> int:
        
        # k in quick_select is 0 indexed
        def quick_select(seq: Sequence[Any], k: int, reverse: bool = False) -> Any:
            seq = seq.copy()
            
            def partition(low: int, high: int) -> int:
                pivot_index, pivot = low, seq[low]
                
                while low <= high:
                    if (seq[low] < pivot if reverse else seq[low] > pivot):
                        seq[low], seq[high] = seq[high], seq[low]
                        high -= 1
                    else:
                        low += 1
                
                seq[high], seq[pivot_index] = seq[pivot_index], seq[high]
                return high
            
            i, j = 0, len(seq) - 1
            x = -1
            while x != k:
                x = partition(i, j)
                if x < k: i = x + 1
                elif x > k: j = x - 1
            
            return seq[x]
        
        return quick_select(nums, k_ - 1, reverse=True)
