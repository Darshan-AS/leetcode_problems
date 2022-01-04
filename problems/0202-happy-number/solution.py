class Solution:
    def isHappy(self, n: int) -> bool:
        # Floyd's Cycle-Finding Algorithm
        get_next = lambda x: sum(map(lambda num: num * num, map(int, str(x))))
        
        walker, runner = n, get_next(n)
        while runner != 1 and runner != walker:
            walker = get_next(walker)
            runner = get_next(get_next(runner))
        
        return runner == 1
        
