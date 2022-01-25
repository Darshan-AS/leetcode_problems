class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        next_num = deque()
        
        c = 1
        for x in reversed(digits):
            c, y = divmod(x + c, 10)
            next_num.appendleft(y)
        
        if c: next_num.appendleft(c)
        
        return next_num
