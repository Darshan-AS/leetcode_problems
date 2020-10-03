class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:        
        num_index = {num: index for index, num in enumerate(nums)}
        
        sol = set()
        for i, n in enumerate(nums):
            for x in [(n - k), (n + k)]:
                if x in num_index and num_index[x] != i:
                    sol.add((n, x) if n < x else (x, n))
        return len(sol)
