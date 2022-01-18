class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        
        left_pass  = list(accumulate(
            range(n),
            lambda a, x: (a[0] + 1, a[1]) if s[x] == '(' else ((a[0], a[1] + 1) if a[0] > a[1] else (0, 0)),
            initial=(0, 0),
        ))
        
        right_pass = list(accumulate(
            range(n - 1, -1, -1),
            lambda a, x: (a[0], a[1] + 1) if s[x] == ')' else ((a[0] + 1, a[1]) if a[0] < a[1] else (0, 0)),
            initial=(0, 0),
        ))
        
        return max(map(sum, filter(lambda c: c[0] == c[1], chain(left_pass, right_pass))))
