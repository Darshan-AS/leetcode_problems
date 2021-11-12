class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def find_sum(index, selected, rem_target):
            if rem_target == 0:
                yield selected.copy()
            
            if rem_target < 0: return
            
            seen = set()
            for i in range(index, len(candidates)):
                if candidates[i] in seen: continue
                else: seen.add(candidates[i])
                
                selected.append(candidates[i])
                yield from find_sum(i + 1, selected, rem_target - candidates[i])
                selected.pop()
            
        return list(find_sum(0, [], target))
