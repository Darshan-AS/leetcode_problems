class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        # if n < 3: return False
        
        i = 1
    
        while i < n and arr[i - 1] < arr[i]: i += 1
        if i in (1, n): return False
        
        while i < n and arr[i - 1] > arr[i]: i += 1
        if i < n: return False
        
        return True
