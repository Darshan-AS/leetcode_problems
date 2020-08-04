import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return math.log(num, 4).is_integer() if num > 0 else False
