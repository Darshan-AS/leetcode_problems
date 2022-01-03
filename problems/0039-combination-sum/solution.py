class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        def combination_sum(index: int, rem_target: int):
            if rem_target == 0:
                yield ()
                return
            
            if not (0 <= rem_target and 0 <= index < len(candidates)):
                return
            
            x = candidates[index]
            yield from (chain((x,), c) for c in combination_sum(index, rem_target - x))
            yield from combination_sum(index + 1, rem_target)
            
        return list(map(list, combination_sum(0, target)))

