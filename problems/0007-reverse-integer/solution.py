class Solution:
    def reverse(self, original_x: int) -> int:
        x, new_x = abs(original_x), 0
        while x:
            new_x = new_x * 10 + x % 10
            x = x // 10
            
        if new_x > 2 ** 31: return 0
        return new_x if original_x >= 0 else -new_x
