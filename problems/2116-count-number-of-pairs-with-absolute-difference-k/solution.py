class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        def two_diff(seq: Sequence[int], target: int) -> Iterator[tuple[int, int]]:
            seen = defaultdict(int)
            
            for x in seq:
                y = target + x
                yield from ((y, x),) * seen[y]
                seen[x] += 1
        
        return sum(1 for _ in chain(two_diff(nums, k), two_diff(nums, -k)))
