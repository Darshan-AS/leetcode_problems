class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        sol = []
        
        def find_sum(index, selected, rem_target):
            if len(selected) > k or rem_target < 0: return
            
            if len(selected) == k and rem_target == 0:
                sol.append(selected.copy())
                return 
            
            for i in range(index, 10):
                if i > rem_target: break
                
                selected.append(i)
                find_sum(i + 1, selected, rem_target - i)
                selected.pop()
            
        find_sum(1, [], n)
        return sol
