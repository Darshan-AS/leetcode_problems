import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x % 10 == 0:
            return False
        
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
        
        if rev < 10:
            return x == rev
        
        return x == rev or x == rev // 10
