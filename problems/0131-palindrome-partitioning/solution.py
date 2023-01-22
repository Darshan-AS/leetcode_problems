from collections.abc import *

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)

        @cache
        def is_sub_str_palindrome(start: int, end: int) -> bool:
            l_to_r = (s[i] for i in range(start, end))
            r_to_l = (s[i] for i in range(end - 1, start - 1, -1))
            return all(map(eq, l_to_r, r_to_l))

        def partition_from(i: int):
            yield from (
                (ps.appendleft(s[i: j]) or ps)
                for j in range(i + 1, n + 1)
                if is_sub_str_palindrome(i, j)
                for ps in partition_from(j)
            ) if i < n else (deque(),)
        
        return list(partition_from(0))
            
