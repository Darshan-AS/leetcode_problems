class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False
        
        reverse_x = 0
        while x > reverse_x:
            reverse_x = reverse_x * 10 + x % 10
            x = x // 10
            
        return x == reverse_x or x == reverse_x // 10
