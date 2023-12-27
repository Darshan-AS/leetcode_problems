class Solution:
    def minCost(self, colors: str, needed_time: list[int]) -> int:
        def colorize(a, x):
            (total_t, prev_c, prev_t), (c, t) = a, x
            return (
                (total_t, c, t) if c != prev_c else 
                (total_t + min(prev_t, t), c, max(prev_t, t))
            )
        
        return reduce(colorize, zip(colors, needed_time), (0, '', 0))[0]
            
