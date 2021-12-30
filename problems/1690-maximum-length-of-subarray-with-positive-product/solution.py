class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def count_next(a: tuple[int, int], x: int) -> tuple[int, int]:
            positive_len, negative_len = a
            if x > 0:
                return positive_len + 1, (negative_len + 1 if negative_len > 0 else 0)
            elif x < 0:
                return (negative_len + 1 if negative_len > 0 else 0), positive_len + 1
            else:
                return 0, 0  
        
        return max(accumulate(nums, count_next, initial=(0, 0)))[0]
