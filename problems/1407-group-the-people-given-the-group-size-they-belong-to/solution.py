class Solution:
    def groupThePeople(self, group_sizes: list[int]) -> list[list[int]]:
        T = TypeVar('T')
        def divide(xs: Sequence[T], k: int) -> Iterator[Sequence[T]]:
            """Divide sequence xs into smaller sequence of length k"""
            return (xs[i : i + k] for i in range(ceil(len(xs) / k)))
        
        groups = reduce(
            lambda a, x: a[x[1]].append(x[0]) or a,
            enumerate(group_sizes),
            defaultdict(list),
        )

        return list(chain.from_iterable((divide(xs, g) for g, xs in groups.items())))
