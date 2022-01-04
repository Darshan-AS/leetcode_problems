class Solution:
    def isHappy(self, n: int) -> bool:
        # There is only one cycle possible
        cycle_numbers = {4, 16, 37, 58, 89, 145, 42, 20}
        
        get_next = lambda x: sum(map(lambda num: num * num, map(int, str(x))))
        
        while n != 1 and n not in cycle_numbers:
            n = get_next(n)
        
        return n == 1
        
