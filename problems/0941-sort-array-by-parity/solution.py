class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        sortedA = [0] * len(A)
        front, rear = 0, len(A) - 1
        
        for i in A:
            if i % 2:
                sortedA[rear] = i
                rear -= 1
            else:
                sortedA[front] = i
                front += 1
        
        return sortedA
