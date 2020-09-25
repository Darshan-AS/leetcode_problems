class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        class NumKey(str):
            def __lt__(x, y):
                return x + y < y + x
        
        ans = ''.join(sorted(map(str, nums), key=NumKey, reverse=True)).lstrip('0')
        return ans if ans else '0' 
