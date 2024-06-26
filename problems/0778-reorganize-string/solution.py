class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        
        counts = Counter(s)
        is_possible = counts.most_common(1)[0][1] <= n // 2 + n % 2

        head = counts.most_common(1)[0]; counts[head[0]] = 0
        chars = chain.from_iterable(starmap(repeat, chain((head,), counts.items())))
        idxs = chain(range(0, n, 2), range(1, n, 2))

        rearranged = reduce(lambda a, x: setitem(a, x[0], x[1]) or a, zip(idxs, chars), [''] * n)
        return ''.join(rearranged) if is_possible else ''
                
