class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        degrees = [[0, 0] for _ in range(n + 2)]    # [indegree, outdegree] of every node
        degrees[0] = [-1, -1]                       # Impossible judge
        degrees[-1] = [n - 1, 0]                    # Default judge
        
        for a, b in trust:
            degrees[a][1] += 1
            degrees[b][0] += 1
        
        judge = degrees.index([n - 1, 0])
        return judge if judge <= n else -1

