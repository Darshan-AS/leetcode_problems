class Solution:
    def isUgly(self, num: int) -> bool:
        def compose(*functions):
            return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

        def repeated_divide(n, k):
            while n and n % k == 0:
                n = n // k
            return n
        
        
        return compose(*(partial(repeated_divide, k=i) for i in (2, 3, 5)))(num) == 1
