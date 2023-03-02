class Solution:
    def compress(self, chars: list[str]) -> int:
        iter_len = lambda xs: sum(1 for _ in xs)
        
        ch_counts = ((ch, iter_len(g)) for ch, g in groupby(chars))
        compressed = chain.from_iterable(ch + str(n) if n > 1 else ch for ch, n in ch_counts)

        i = 0
        for i, ch in enumerate(compressed): chars[i] = ch
        return i + 1
