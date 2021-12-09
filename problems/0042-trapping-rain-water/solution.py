class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = list(accumulate(height, lambda a, x: max(a, x)))
        right_max = list(reversed(list(accumulate(reversed(height), lambda a, x: max(a, x)))))
        
        return sum(min(lm, rm) - h for h, lm, rm in zip(height, left_max, right_max))
