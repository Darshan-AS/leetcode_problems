class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        
        def find_sum(index, selected, rem_target):
            if rem_target == 0:
                sol.append(selected.copy())
                return 
            
            if rem_target < 0: return
            
            for i in range(index, len(candidates)):
                selected.append(candidates[i])
                find_sum(i, selected, rem_target - candidates[i])
                selected.pop()
            
        find_sum(0, [], target)
        return sol
