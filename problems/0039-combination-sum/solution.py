class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        prefix = []
        n = len(candidates)
        
        def dfs(index, k):
            if candidates[index] > k:
                return
            elif (x := candidates[index]) == k:
                sol.append(prefix + [x])
                return
            
            prefix.append(candidates[index])
            for i in range(index, n):
                dfs(i, k - candidates[index])
            prefix.pop()
        
        for i in range(n):
            dfs(i, target)
        return sol
