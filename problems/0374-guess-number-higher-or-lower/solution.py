# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        
        while low <= high:
            mid = (low + high) // 2
            
            result = guess(mid)
            if result == 1:
                low = mid + 1
            elif result == -1:
                high = mid - 1
            else:
                return mid
        
        return -1
