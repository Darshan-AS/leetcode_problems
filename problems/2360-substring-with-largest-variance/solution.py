class Solution:
    def largestVariance(self, s: str) -> int:
        def variance(major: str, minor: str, rem_minors: int) -> int:
            encoder = partial(getitem, defaultdict(int, {major: 1, minor: -1}))
            encoded_s = filter(bool, map(encoder, s))

            next_ = lambda st, x: tuple(map(add, (x > 0, x < 0, min(x, 0)), ((0, 0, st[2]) if st[0] < st[1] and st[2] > 0 else st)))
            states = accumulate(encoded_s, next_, initial=(0, 0, rem_minors)) # init_st = (major_count, minor_count, remaining_minor_count)

            return max((mjr - mnr for mjr, mnr, _ in states if mnr > 0), default=0)
        
        c = Counter(s)
        return max(variance(mjr, mnr, c[mnr]) for mjr, mnr in product(ascii_lowercase, ascii_lowercase))
