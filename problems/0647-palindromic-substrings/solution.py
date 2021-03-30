class Solution:
    def count_palindrome_around_center(self, s: str, left: int, right: int) -> int:
        n = len(s)
        
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        
        return ceil((right - left - 1) / 2)
    
    def countSubstrings(self, s: str) -> int:
        return sum(
            self.count_palindrome_around_center(s, i, i) + 
            self.count_palindrome_around_center(s, i, i + 1) 
            for i in range(len(s))
        )
            

