class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def num_distinct_helper(s_i: int=0, t_i: int=0) -> int:
            if t_i == len(t):
                return 1

            if s_i == len(s):
                return 0

            if s[s_i] == t[t_i]:
                return num_distinct_helper(s_i + 1, t_i + 1) + num_distinct_helper(s_i + 1, t_i)
            else:
                return num_distinct_helper(s_i + 1, t_i)
        
        return num_distinct_helper()
