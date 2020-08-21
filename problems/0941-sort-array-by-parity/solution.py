class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        
        while i <= j:
            if A[i] % 2 and not A[j] % 2:
                A[i], A[j] = A[j], A[i]
            
            if not A[i] % 2: i += 1
            if A[j] % 2: j -= 1
        
        return A
