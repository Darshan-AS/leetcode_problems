class Solution:
    def convert(self, s: str, k: int) -> str:
        if k == 1:
            return s
        
        ans = []
        n = len(s)
        for i in range(k):
            j = i
            
            middle = True
            while j < n:
                ans.append(s[j])
                if i == 0 or i == k - 1:
                    j += 2 * (k - 1)
                else:
                    j += 2 * (k - i - 1) if middle else 2 * i
                    middle = not middle
                
        return ''.join(ans)
