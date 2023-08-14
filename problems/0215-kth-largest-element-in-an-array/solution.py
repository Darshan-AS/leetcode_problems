class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        T, V = TypeVar('T'), TypeVar('V')
        Key = Callable[[T], V]

        def quick_select(seq: Sequence[T], k: int, key: Key = None, reverse: bool = False) -> T:
            pivot = choice(seq)
            key = (lambda x: x) if key is None else key
            cmp = lambda x: ((key(x) > key(pivot)) - (key(x) < key(pivot))) * (-1 if reverse else 1)

            mids, rights, lefts = reduce(lambda a, x: a[cmp(x)].append(x) or a, seq, ([], [], []))
            nl, nr = len(lefts), len(lefts) + len(mids)

            if k <= nl: return quick_select(lefts , k, key, reverse)
            if k >  nr: return quick_select(rights, k - nr, key, reverse)
            return pivot

        return quick_select(nums, k, reverse=True)
