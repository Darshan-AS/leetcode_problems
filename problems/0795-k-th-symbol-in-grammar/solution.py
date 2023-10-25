class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def kth(k: int) -> int:
            return k and kth(k // 2) ^ (k % 2)
        
        return kth(k - 1)


        

