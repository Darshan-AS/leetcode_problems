class Solution:
    def maxArea(self, h: int, w: int, h_cuts: List[int], v_cuts: List[int]) -> int:
        def pairwise(iterable):
            a, b = tee(iterable)
            next(b, None)
            return zip(a, b)
            
        max_cut = lambda cuts: max(map(lambda x: x[1] - x[0], pairwise(sorted(cuts))))
        
        M = 1_000_000_007
        return max_cut(chain(h_cuts, (0, h))) % M * max_cut(chain(v_cuts, (0, w))) % M
