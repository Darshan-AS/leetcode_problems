class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        @cache
        def turns(l, r):
            j = -1
            ans = inf
            for i in range(l, r):
                if s[i] != s[r] and j == -1: j = i
                if j != -1: ans = min(ans, 1 + turns(j, i) + turns(i + 1, r))
            return 0 if j == -1 else ans

        return turns(0, n - 1) + 1
