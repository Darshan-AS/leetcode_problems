class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        def find_sum(index, selected, rem_target):
            if rem_target == 0:
                yield selected.copy()
            
            if rem_target < 0: return
            
            for i in range(index, len(candidates)):
                selected.append(candidates[i])
                yield from find_sum(i, selected, rem_target - candidates[i])
                selected.pop()
            
        return list(find_sum(0, [], target))

