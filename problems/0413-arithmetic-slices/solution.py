class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Available in itertools in version >= 3.10
        def pairwise(iterable):
            a, b = tee(iterable)
            next(b, None)
            return zip(a, b)
        
        def count_equals(iterable):
            count = 1
            a = next(iterable, None)
            b = next(iterable, None)
            while b is not None:
                if a != b:
                    yield count
                    count = 0
                
                count += 1
                a, b = b, next(iterable, None)
            yield count
        
        def subset_count(n: int) -> int:
            return (n * (n + 1) // 2) - n - (n - 1)
        
        return sum(map(
            lambda x: subset_count(x + 1), 
            count_equals(b - a for a, b in pairwise(nums))
        ))

