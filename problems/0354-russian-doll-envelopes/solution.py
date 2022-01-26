class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def lis_len(iterable) -> int:
            lis = []
            
            for x in iterable:
                if not lis or lis[-1] < x:
                    lis.append(x)
                else:
                    lis[bisect_left(lis, x)] = x
            
            return len(lis)
        
        s_envelopes = sorted(envelopes, key=lambda e: (e[0], -e[1]))
        return lis_len(map(itemgetter(1), s_envelopes))
        
