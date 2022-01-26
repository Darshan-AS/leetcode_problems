class Solution:
    @cache
    def superEggDrop(self, k: int, n: int) -> int:
        if n <= 1 or k == 1: return n
        
        low, high = 1, n
        
        while low <= high:
            i = (low + high) // 2
            
            x = self.superEggDrop(k - 1, i - 1)
            y = self.superEggDrop(k, n - i)
            
            if x < y:
                low = i + 1
            elif x > y:
                high = i - 1
            else:
                return 1 + max(x, y)
            
        return 1 + min(
            max(self.superEggDrop(k - 1, low - 1), self.superEggDrop(k, n - low)),
            max(self.superEggDrop(k - 1, high - 1), self.superEggDrop(k, n - high)),
        )
