class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        T = TypeVar('T')

        def split_count(xs: Iterable[T], d: T) -> Iterator[int]:
            c = 0
            for x in xs:
                if x == d: yield c
                c = 0 if x == d else c + 1
            yield c
        
        return max(starmap(add, pairwise(split_count(nums, 0))), default=len(nums) - 1)
