class Solution:
    def compress(self, chars: list[str]) -> int:
        count = lambda xs: str(k) if (k := sum(1 for _ in xs)) > 1 else ''
        compressed = (x for ch, g in groupby(chars) for x in ch + count(g))
        for i, x in enumerate(compressed): chars[i] = x
        return i + 1
