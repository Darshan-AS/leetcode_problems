class Solution:
    def minMaxDifference(self, num: int) -> int:
        def replace_num(n: int, a: int, b: int) -> int:
            return int(''.join(str(b) if int(x) == a else x for x in str(n)))
        
        xs = tuple(replace_num(num, i, j) for i, j in product(range(10), range(10)))
        return max(xs) - min(xs)
