class Solution:
    def countAndSay(self, n: int) -> str:
        len_ = lambda iterable: sum(1 for _ in iterable)
        
        def say(s: str) -> str:
            return ''.join(str(len_(g)) + i for i, g in groupby(s))
        
        return reduce(lambda a, _: say(a), range(1, n), '1')
