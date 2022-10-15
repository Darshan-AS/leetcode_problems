class Solution:
    def compress(self, chars: list[str]) -> int:
        T = TypeVar('T')
        TCount = Tuple[T, int]
        def group_count(ts: Iterable[T]) -> Iterator[TCount]:
            ts = iter(ts)
            try:
                prev_t, count = next(ts), 1
            except StopIteration:
                return
            
            for t in ts:
                if t != prev_t:      
                    yield (prev_t, count)
                    prev_t, count = t, 0
                count += 1
            yield (prev_t, count)
        
        compressed_chars = chain.from_iterable(ch + str(count) if count > 1 else ch for ch, count in group_count(chars))
        
        for i, ch in enumerate(compressed_chars):
            chars[i] = ch
        return i + 1
