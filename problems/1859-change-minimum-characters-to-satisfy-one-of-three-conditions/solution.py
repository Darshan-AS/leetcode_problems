class Solution:
    def minCharacters(self, s1: str, s2: str) -> int:
        def lt_eq_gt_counter(seq, sorted_pool=None):
            n = len(seq)
            c = Counter(seq)
            sorted_pool = sorted(c.keys()) if sorted_pool is None else sorted_pool
            
            values = accumulate(
                sorted_pool,
                lambda a, x: (a[0] + a[1], c[x], a[2] - c[x]),
                initial=(0, 0, n)
            )
            
            next(values)
            return dict(zip(sorted_pool, values))
        
        s1_counter = lt_eq_gt_counter(s1, ascii_lowercase)
        s2_counter = lt_eq_gt_counter(s2, ascii_lowercase)
        
        s1_values = iter(s1_counter.values())
        s2_values = iter(s2_counter.values())
        c1a, c2a = next(s1_values), next(s2_values)
        
        except_a_min = min(map(
            lambda c1, c2: min(
                c1[1] + c1[2] + c2[0],
                c1[0] + c2[1] + c2[2],
                c1[0] + c1[2] + c2[0] + c2[2],
            ),
            s1_values,
            s2_values,
        ))
        
        return min(except_a_min, c1a[0] + c1a[2] + c2a[0] + c2a[2])
