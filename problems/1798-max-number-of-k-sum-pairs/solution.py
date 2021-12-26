class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        def unique_two_sum_pairs(seq: Sequence[int], target: int) -> Iterator[tuple[int, int]]:
            seen = defaultdict(int)
            
            for x in seq:
                if seen[(y := target - x)]:
                    yield (y, x)
                    seen[y] -= 1
                else:
                    seen[x] += 1
        
        return sum(1 for _ in unique_two_sum_pairs(nums, k))
                    
