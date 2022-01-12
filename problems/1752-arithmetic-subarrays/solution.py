class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:        
        def is_arithmetic(iterable: iter) -> bool:
            a, b = tee(iterable)
            next(a, None)
            return len(set(map(operator.sub, a, b))) == 1
        
        return [is_arithmetic(sorted(nums[i: j + 1])) for i, j in zip(l, r)]
