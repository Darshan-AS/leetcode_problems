class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        degrees = list(chain((-1,), repeat(0, n), (n - 1,)))
        
        for u, v in trust: degrees[u] -= 1; degrees[v] += 1
        
        judge = degrees.index(n - 1)
        return judge if judge <= n else -1

