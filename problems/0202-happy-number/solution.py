class Solution:
    def isHappy(self, n: int) -> bool:
        # There is only one cycle possible and any member is guaranteed to be visited
        cycle_member = 4
        
        get_next = lambda x: sum(map(lambda num: num * num, map(int, str(x))))
        
        while n != 1 and n != cycle_member:
            n = get_next(n)
        
        return n == 1
        
