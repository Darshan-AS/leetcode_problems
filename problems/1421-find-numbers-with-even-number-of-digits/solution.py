class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def digit_len(n: int) -> int:
            length = 0
            while n:
                n //= 10
                length += 1
            return length
        
        return sum(map(lambda num: digit_len(num) % 2 == 0, nums))
