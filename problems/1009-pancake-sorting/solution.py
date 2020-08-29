class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        k_indices = []
        
        for i in range(len(A) - 1, -1, -1):
            k_max = max(range(i + 1), key=A.__getitem__)
            k_indices.append(k_max + 1)
            A = A[k_max::-1] + A[k_max + 1:]
            k_indices.append(i + 1)
            A = A[i::-1] + A[i + 1:]
        
        return k_indices

