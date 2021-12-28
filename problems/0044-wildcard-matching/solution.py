class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def is_match(s_i: int, p_i: int) -> bool:
            if s_i < 0 and p_i < 0: return True
            if p_i < 0: return False
            if s_i < 0: return all(p[i] == '*' for i in range(p_i, -1, -1))

            if s[s_i] == p[p_i] or p[p_i] == '?':
                return is_match(s_i - 1, p_i - 1)
            elif p[p_i] == '*':
                return any((is_match(s_i - 1, p_i - 1), is_match(s_i - 1, p_i), is_match(s_i, p_i - 1)))
            else:
                return False
        
        return is_match(len(s) - 1, len(p) - 1)
