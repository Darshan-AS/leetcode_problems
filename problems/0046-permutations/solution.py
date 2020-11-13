from itertools import chain

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        full_mask = 2 ** n - 1
        
        def permutation(mask=0):
            if mask == full_mask: yield iter([])
            
            for i in range(n):
                if mask & (1 << i): continue
                for p in permutation(mask | (1 << i)):
                    yield chain([nums[i]], p)

        return list(map(list, permutation()))
