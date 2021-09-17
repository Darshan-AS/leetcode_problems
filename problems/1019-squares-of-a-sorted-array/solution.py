class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        origin = bisect.bisect_left(nums, 0)
        i, j = origin - 1, origin
        
        squares = []
        while i >= 0 and j < len(nums):
            x = min(-nums[i], nums[j])
            i, j = (i - 1, j) if -nums[i] < nums[j] else (i, j + 1)
            squares.append(x ** 2)
        
        while i >= 0: 
            squares.append(nums[i] ** 2)
            i -= 1
        
        while j < len(nums):
            squares.append(nums[j] ** 2)
            j += 1
        
        return squares
