class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        edge_count = {i: [0, 0] for i in range(1, N + 1)}
        
        for i, j in trust:
            edge_count[i][1] += 1
            edge_count[j][0] += 1
        
        for k, v in edge_count.items():
            if v == [N - 1, 0]:
                return k
        return -1
