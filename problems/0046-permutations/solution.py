class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        T = TypeVar('T')
        def permutations(pool: Iterable[T], r: int = None) -> Iterator[Iterator[T]]:
            pool = tuple(pool)
            r = len(pool) if r is None else r

            yield from (
                (x,) + p
                for i, x in enumerate(pool)
                for p in permutations(pool[:i] + pool[i + 1:], r - 1)
            ) if pool and r else ((),)
        
        return list(permutations(nums))
