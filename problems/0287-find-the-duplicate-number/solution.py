class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        T = TypeVar('T')
        def iter_indexed(xs: Sequence[T], idx: int = 0) -> Iterator[T]:
            while (idx := xs[idx]): yield idx
        
        walker_nodes = iter_indexed(nums)
        runner_nodes = compress(iter_indexed(nums), cycle((0, 1)))
        
        meet = next(w for w, r in zip(walker_nodes, runner_nodes) if w == r)
        return next(a for a, b in zip(iter_indexed(nums), iter_indexed(nums, meet)) if a == b)
