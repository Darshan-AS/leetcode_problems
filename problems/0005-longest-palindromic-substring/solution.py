class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_i, ans_j = 0, 1
        
        for k in range(2 * len(s) - 1):
            x = k // 2
            i = x if k % 2 else x - 1
            j = x + 1
            
            while i >= 0. and j < len(s) and  s[i] == s[j]:
                i, j = i - 1, j + 1
                
            if j - i - 1 > ans_j - ans_i:
                ans_i, ans_j = i + 1, j
            
        return s[ans_i:ans_j]
