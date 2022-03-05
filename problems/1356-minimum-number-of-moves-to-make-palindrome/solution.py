class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        moves = 0
        while s:
            i = s.index(s[-1])
            if i == len(s) - 1: moves += len(s) // 2; s = s[:-1]
            else: moves += i; s = s[:i] + s[i + 1: -1]
        
        return moves
