class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        candidates.sort()
        
        def find_sum(index, selected, rem_target):
            if rem_target == 0:
                sol.append(selected.copy())
                return 
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i - 1] == candidates[i]: continue
                if candidates[i] > rem_target: break
                
                selected.append(candidates[i])
                find_sum(i + 1, selected, rem_target - candidates[i])
                selected.pop()
            
        find_sum(0, [], target)
        return sol
