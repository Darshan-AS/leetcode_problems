class Solution:
    
    def ncr(self, n, r):
        ans = 1
        for i in range(n, n - r, -1):
            ans *= i
        for i in range(r, 1, -1):
            ans //= i
        return ans
    
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [self.ncr(rowIndex, r) for r in range((rowIndex // 2) + 1)]
        if not rowIndex:
            return ans
        return ans + ans[::-1] if rowIndex % 2 else ans + ans[-2::-1]

