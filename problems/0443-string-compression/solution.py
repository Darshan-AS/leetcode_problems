class Solution:
    def compress(self, chars: list[str]) -> int:
        T = TypeVar('T') # This should be Comparables, i.e types with __eq__
        TCount = tuple[T, int]

        def group_count(iterable: Iterable[T]) -> Iterator[TCount]:
            xs = iter(iterable)
            sentinal = object()

            z, n = next(xs, sentinal), 1
            for x in xs:
                if x != z:
                    yield (z, n)
                    z, n = x, 0
                n += 1
            
            if z != sentinal: yield (z, n)
        
        compressed = chain.from_iterable(
            ch + str(n) if n > 1 else ch
            for ch, n in group_count(chars)
        )

        i = 0
        for i, ch in enumerate(compressed): chars[i] = ch
        return i + 1
