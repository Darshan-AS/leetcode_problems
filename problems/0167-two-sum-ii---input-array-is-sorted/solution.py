from bisect import bisect_left, bisect_right

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ > target:
                right = bisect_right(numbers, target - numbers[left], left, right - 1)
                # right -= 1
            elif sum_ < target:
                left = bisect_left(numbers, target - numbers[right], left + 1, right)
                # left += 1
            else:
                return [left + 1, right + 1]
        
