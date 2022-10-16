class Solution:
    def minDifficulty(self, diffs: list[int], d_: int) -> int:
        @cache
        def min_diff(i: int, d: int):
            if d == 1: return max(diffs[i:])
            
            return min((
                max(diffs[i:k]) + min_diff(k, d - 1)
                for k in range(i + 1, len(diffs))),
                default=inf,
            )
        
        m_diff = min_diff(0, d_)
        return -1 if m_diff == inf else m_diff
